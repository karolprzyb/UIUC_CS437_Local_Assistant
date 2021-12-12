#include "esphome.h"


class KaufLight : public Component, public LightOutput {
 public:

  FloatOutput *output_red;
  FloatOutput *output_green;
  FloatOutput *output_blue;
  FloatOutput *output_cold;
  FloatOutput *output_warm;

  float min_mireds = 150;
  float max_mireds = 350;

  float max_white = .75;
  float max_blue  = .6;

  float last_ct = .5;

  void setup() override {

  }

  LightTraits get_traits() override {

    // return the traits this light supports
    auto traits = LightTraits();
    traits.set_min_mireds(min_mireds); 
    traits.set_max_mireds(max_mireds); 
    traits.set_supported_color_modes({ColorMode::RGB, ColorMode::COLOR_TEMPERATURE});
    return traits;
  }



  void write_state(LightState *state) override {

    float red, green, blue;
    float ct, white_brightness;
    float brightness;

    // get rgbww values
    state->current_values_as_rgb(&red, &green, &blue);
    state->current_values_as_ct(&ct, &white_brightness);
    state->current_values_as_brightness(&brightness);

    // ESP_LOGD("Kauf Light", "----------------------------------------------" );
    // ESP_LOGD("Kauf Light", "----------------------------------------------" );
    // ESP_LOGD("Kauf Light", "----------------------------------------------" );
    // ESP_LOGD("Kauf Light", "----------------------------------------------" );
    // ESP_LOGD("Kauf Light", "------------- INPUT FROM ESPHOME -------------" );
    // ESP_LOGD("Kauf Light", "----------------------------------------------" );
    // ESP_LOGD("Kauf Light", "       RGB:   R:%f ||   G:%f ||  B:%f", red, green, blue );
    // ESP_LOGD("Kauf Light", "        CT:  CT:%f || LCT:%f", ct, last_ct );
    // ESP_LOGD("Kauf Light", "BRIGHTNESS:  WB:%f ||   B:%f", white_brightness, brightness );

    // ESP_LOGD("Kauf Light", "----------------------------------------------" );
    // ESP_LOGD("Kauf Light", "------------------- OUTPUT -------------------" );
    // ESP_LOGD("Kauf Light", "----------------------------------------------" );

    // if light is off, just set all outputs to 0 and exit
    if ( (brightness==0) && (white_brightness==0) ) {
      this->output_red->set_level(0);
      this->output_green->set_level(0);
      this->output_blue->set_level(0);
      this->output_cold->set_level(0);
      this->output_warm->set_level(0);

      // ESP_LOGD("Kauf Light", "Light Off" );
      return;
    }



    // if ct set
    if ( white_brightness!=0 ) {

      // store ct for use in rgb calculation
      last_ct = ct;

      // no rgb
      this->output_red->set_level(0);
      this->output_green->set_level(0);
      this->output_blue->set_level(0);

      // warm level is ct variable, cold level is inverse ct, scaled to white_brightness
      this->output_cold->set_level((1-ct) * white_brightness);
      this->output_warm->set_level(ct * white_brightness);

      // ESP_LOGD("Kauf Light", "Color Temp: %f || White Brightness: %f", ct, white_brightness );

      return;
    }



    // if rgb set

    // get minimum value of r, g, and b for combining RGB values to white
    float min_val;
    if ( (red <= green) && (red <= blue) ) { min_val = red; } else
    if ( green <= blue )                  { min_val = green; } else
                                         { min_val = blue; }

    // combine RGB values into white value 
    float scaled_red   = red   - min_val;
    float scaled_green = green - min_val;
    float scaled_blue  = (blue  - min_val) * max_blue;   // scale blue to whatever setting is
    float scaled_white = min_val * max_white;            // scale white to whatever setting is

    // Proportion between cold/warm is based on last ct setting.  Total scaled cold+warm = scaled_white
    float scaled_cold = scaled_white*(1-last_ct);
    float scaled_warm = scaled_white*last_ct;


    // ESP_LOGD("Kauf Light", "R:%f || G: %f || B:%f || W:%f --> CW:%f || WW:%f)", scaled_red, scaled_green, scaled_blue, scaled_white, scaled_cold, scaled_warm);

    this->output_red->set_level(scaled_red);
    this->output_green->set_level(scaled_green);
    this->output_blue->set_level(scaled_blue);
    this->output_cold->set_level(scaled_cold);
    this->output_warm->set_level(scaled_warm);

    return;
  }

};