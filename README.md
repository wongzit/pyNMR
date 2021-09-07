# py.NMR
![](pyNMR_rm.png)
py.**NMR** is a Python program for easily applying scaling factor to computed magnetic shielding 
tensors.

## Usage

py.**NMR** reads a Gaussian output of NMR calculation and extracting magnetic shielding 
tensor (the isotropic value) from output. When users run py.**NMR**, a specification of output 
path is necessary.

```
Gaussian output file:
(e.g.: /pyNMR/examples/benzene.log)
/Users/wangzhe/Desktop/az_cs2021.log 
```

Then, users need to specify the element symbol of which element will be investigated. For 1H NMR, 
input: "H", and press ENTER key. The element symbol is case-sensitive, "Ca" and "ca" are different. 
After that, the magnetic shielding tensors (in ppm) will be displayed.

```
Please specify the element (case-sensitive): H

  No.      Atom       Sigma (ppm)
-----------------------------------
    5        H           27.1579
    7        H           27.8845
   13        H           28.8314
   14        H           29.6048
   15        H           29.1709
   17        H           29.0782
   18        H           28.8309
   19        H           28.5883
   26        H           23.9736
   27        H           22.8661
   28        H           24.0874
   29        H           23.9366
   36        H           23.2589
   37        H           23.9442
   38        H           24.1095
   39        H           23.9661
   50        H           24.0595
   51        H           23.2576
   52        H           24.0859
   53        H           23.8234
   60        H           23.3369
   61        H           24.1041
   62        H           24.0658
   63        H           23.8437
   65        H           23.1876
   72        H           23.7747
   73        H           23.5156
   74        H           23.5790
   76        H           23.1841
   78        H           23.6839
   81        H           29.4230
   82        H           29.2679
   84        H           25.9964
   86        H           25.9800
-----------------------------------
```

If user inputted an element which was not existed in the output, or non-element character, program 
will be terminated with an error message:

```
Did not find element X, program termination.
```

The NMR scaling factor could be applied to get more accurate chemical shift. To apply the scaling factor, 
input "y" in following message:

```
Apply scaling fator? (y/n): y
```

Then, users need to specify the scaling factor, slope and intercept, and press ENTER key. The scaled chemical 
shift (in ppm) will be displayed in current windows.

```
Please specify the slope and intercept:
-1.0592 31.9654

  No.      Atom       Delta (ppm)
-----------------------------------
    5        H            4.5388
    7        H            3.8528
   13        H            2.9588
   14        H            2.2287
   15        H            2.6383
   17        H            2.7258
   18        H            2.9593
   19        H            3.1883
   26        H            7.5451
   27        H            8.5907
   28        H            7.4377
   29        H            7.5801
   36        H            8.2199
   37        H            7.5729
   38        H            7.4168
   39        H            7.5522
   50        H             7.464
   51        H            8.2211
   52        H            7.4391
   53        H            7.6869
   60        H            8.1462
   61        H            7.4219
   62        H            7.4581
   63        H            7.6678
   65        H            8.2872
   72        H            7.7329
   73        H            7.9775
   74        H            7.9177
   76        H            8.2905
   78        H            7.8186
   81        H            2.4003
   82        H            2.5467
   84        H            5.6354
   86        H            5.6509
-----------------------------------
```

The magnetic shielding tensors (and scaled chemical shift, if avaibable) will be saved as a .txt file in the same dictionary.

```
A .txt file will be saved at same dictionary with the output file.
```

If scaling factors were applied, a .xlsx file would be saved to plot NMR spectrum. The peak broadening is based on Lorentizan function, 
users can draw the scaled NMR spectrum with the data points in saved Excel file. The default parameters for NMR spectrum range is from 9.5 ppm 
to -0.5 ppm, and half-width at half height is 0.01 ppm. Users can modify these parameters by input menu number. The current setting would be 
displayed in command windows, press ENTER to use current parameters.

```
===============================================================
         Scaled NMR spectrum will be saved in .xlsx file
---------------------------------------------------------------
       1 - Spectrum range: from 10.5 to -0.5 ppm
       2 - Peak half-width at half height: 0.01 ppm
===============================================================
Press ENTER to use current setting, or input menu number
  to modify the parameters: 2

Please specify the half-width at half height:
0.03

===============================================================
         Scaled NMR spectrum will be saved in .xlsx file
---------------------------------------------------------------
       1 - Spectrum range: from 10.5 to -0.5 ppm
       2 - Peak half-width at half height: 0.03 ppm
===============================================================
Press ENTER to use current setting, or input menu number
  to modify the parameters: (ENTER)
```

A .xlsx would be saved in the same dictionary. And user can plot the spectrum with these data!
![](/example/az_cs2021_spectrum.jpg)

## Update history
### v2.1 (2021-09-06)
Smaller split value for NMR plot is adapted. (0.001 ppm in v2.1, 0.05 ppm in older versions)

### v2.0 (2021-09-03)
1. Now .txt will be automatically saved in current dictionary.
2. Lorentzian function will be applied to scaled chemical shift and the spectrum data would be saved as a .xlsx file in current dictionary.

### v1.0 (2021-09-03)
Updated UI.

### v0.2 (2021-09-03)

First pre-release of py.**NMR**.
