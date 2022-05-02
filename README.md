# StrucEng_Library

'StrucEng Library' is an add-on package for the open-source, python-based computational framework COMPAS FEA. The 'StrucEng Library' includes mechanical models, saftey concepts, GUI's, load generator, etc. for the strucutral analysis of reinforced concrete and masonry members.

## Models for reinforced concrete
* Sandwichmodel: linear-elastic ideal-plastic analysis of reinforced concrete shell structures 
* CMM-Usermat: ...in progress...
* Cross-section analysis: ...in progress...

## Models for masonry
* URM-Usermat: ...in progress...

## safty concepts
* Partial Safty Factors (PSF): ...in progress...
* Estimate of coefficient of variation: ...in progress...
* Full probabilistic analysis: ...in progress...

## Load generators
* Traffic loads on bridges
* more in progress...




Please check out the following [Link](https://github.com/kfmResearch-NumericsTeam/StrucEng_Library/blob/main/Sandwichmodel/Example/Tutorial.pdf) for the installation and the use of the StrucEng Library. A more detailed Wiki will follow soon ...


 `StrucEng Library`
add-on package for the COMPAS framework.










## Requirements
To work with CMM-Usermat you need the following software:
* ANSYS Mechanical APDL (64 bit)
* A source text editor (we recommend to use [Visual Studio Code](https://code.visualstudio.com/) with the [ansys-apdl-syntax highlighter](https://marketplace.visualstudio.com/items?itemName=smhrjn.ansys-apdl-syntax))
* Matlab

## Order a License
Please send a mail to weber@ibk.baug.ethz.ch including the name of your computer. As soon as possible you will recive a E-Mail with a file called `usermatLib.dll`. You will find out the computer name as describe in the following:
01. Press `Windows`+`R`
02. Type in `cmd` and confirm with `Enter`
03. Type in `hostname` and press `Enter`
04. The sequence of characters and/or numbers is the current name of the computer.

> **NOTE**: The `usermatLib.dll` contains the CMM-Usermat as a single user license valid for 1 year. The CMM-Usermat is currently only available for Windows. 

## Installation
After you installed ANSYS Mechanical APDL and recived the `usermatLib.dll` you have to configurate ANSYS APDL for the use of the CMM-Usermat.

> **NOTE**: In order to allow ANSYS APDL to access User defined Materials, you must select the option `ANSYS Customization Files` during the installation of ANSYS APDL

01. Open the `advanced system settings` on your computer (you may need admin rights). Then click on `Environment Variables`.<br> <br> 
[<img src="https://github.com/kfmResearch-NumericsTeam/auxiliary/blob/main/Figures/CMM-Usermat/Installation%20proceedere/advanced%20system%20setting.jpg">](https://github.com/kfmResearch-NumericsTeam/auxiliary/blob/main/Figures/CMM-Usermat/Installation%20proceedere/advanced%20system%20setting.jpg)

02. Under `System variables` click on `new`. <br> <br> 
[<img src="https://github.com/kfmResearch-NumericsTeam/auxiliary/blob/main/Figures/CMM-Usermat/Installation%20proceedere/Environment%20Variables.jpg">](https://github.com/kfmResearch-NumericsTeam/auxiliary/blob/main/Figures/CMM-Usermat/Installation%20proceedere/Environment%20Variables.jpg)

03. Type in the name of the variable `ANS_USER_PATH` and the value of the variable is C:\Program Files\ANSYS Inc\vXXX\ansys\bin\winx64 (XXX stands for the installed version of ANSYS APDL, e.g. 192 for the version 19.2). Then confirm everything with `OK`. <br> <br>
[<img src="https://github.com/kfmResearch-NumericsTeam/auxiliary/blob/main/Figures/CMM-Usermat/Installation%20proceedere/New%20System%20Variable.jpg">](https://github.com/kfmResearch-NumericsTeam/auxiliary/blob/main/Figures/CMM-Usermat/Installation%20proceedere/New%20System%20Variable.jpg)

04. Copy the `usermatLib.dll` in the folder C:\Program Files\ANSYS Inc\vXXX\ansys\bin\winx64 on your computer. The configuration is now complete.

## Example
More to come soon ...



