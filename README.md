# LabVIEW User Interface Testing framework

The aim of this project is:
1. test several UI scrapping tools available and check if some can be used with a LabVIEW application. 
2. Make a framework (first in Python) to script some user interface testing

# UI scrapping tools

## To test

### Microsoft's UI Automation framework 

C# provides support for UI Automation through the System.Windows.Automation

### WinAppDriver

* [Windows Doc](https://techcommunity.microsoft.com/t5/testingspot-blog/winappdriver-and-desktop-ui-test-automation/ba-p/1124543)
* [GitHub](https://github.com/microsoft/WinAppDriver)

## Tested



# Framework

## 1.0.0

* A subVI call "UI-Tester.vi" need to be added to top level VI. This subVI will encapsulate all the logic needed.
* A python package is made to encapsulate some generic commands
    * front-most : Return the frontmost Window 
    * click-btn : Click on a specific button based on its label on the frontmost Window
    * grab : Get the data/value of a specific object based on its label