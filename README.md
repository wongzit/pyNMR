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
(User input)/Users/wangzhe/Desktop/benzene.log 
```

Then, users need to specify the element symbol of which element will be investigated. For 1H NMR, 
input: "H", and press ENTER key. The element symbol is case-sensitive, "Ca" and "ca" are different. 
After that, the magnetic shielding tensors (in ppm) will be displayed.

```
Please specify the element (case-sensitive): H

  No.      Atom       Sigma (ppm)
-----------------------------------
    7        H           24.1077
    8        H           24.0931
    9        H           24.0925
   10        H           24.1077
   11        H           24.0931
   12        H           24.0925
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
(User input)-1.0781 31.9786

  No.      Atom       Delta (ppm)
-----------------------------------
    7        H            7.3007
    8        H            7.3143
    9        H            7.3148
   10        H            7.3007
   11        H            7.3143
   12        H            7.3148
-----------------------------------
```

If users want to save the magnetic shielding tensors and scaled chemical shift values, input "y" in following message:

```
Save NMR data to .txt file? (y/n): y
```

The data will be saved as a .txt file in current dictionary.

## Update history

### v2.0 (2021-09-03)
1. Now .txt will be automatically saved in current dictionary.
2. Lorentzian function will be applied to scaled chemical shift and the spectrum data would be saved as a .xlsx file in current dictionary.

### v1.0 (2021-09-03)
Updated UI.

### v0.2 (2021-09-03)

First pre-release of py.**NMR**.
