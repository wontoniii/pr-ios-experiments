# pr-ios-experiments

* Install Appium (https://appium.io/docs/en/about-appium/getting-started/index.html)
* Install xcode
* Add your user
* Create certificate
* Plug your ipad / iphone
* Trust device
* Go to Settings > General > Device Management and select the profile to trust (you might need to deploy an app first)
* Open keychain and go to your developer certificate. You should find your user id and organization id
* pip install Appium-Python-Client
* Follow the configuration for a real device: https://github.com/appium/appium-xcuitest-driver/blob/master/docs/real-device-config.md#basic-automatic-configuration
* If it doesn't work try to follow: https://medium.com/tauk-blog/setup-guide-for-appium-real-ios-device-e35eabbf630e
* Parameters for appium: https://github.com/appium/appium-xcuitest-driver/blob/master/README.md#webdriveragent
* If nothing works, install the beta version: https://github.com/appium/appium/issues/17174
* Maybe something interesting can be found here: https://github.com/appium/appium-safari-driver