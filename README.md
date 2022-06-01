# DriverSetup
This package contains several modules:
## DriverSetup
### Description
The `DriverSetup` package is a packed functions from selenium.
### Usage
- Importing the entire module is advised, which is:
`from utility.DriverSetup import *`
By importing *, the `selenium.webdriver.common.by.By` and `selenium.webdriver.support.select.Select` is automatically imported.
- The module use __only Chrome driver__. To run the module correctly, the correspond version of *chromedriver.exe* is required.
### Methods
1. Create driver object `driver = DriverSetup()` : create the selenium driver object, containing all `selenium.webdriver.Chrome` methods.

2. `driver.endDriver(wait)` : takes only one argument `wait:(float)` which indicate the time that keep the browser. default is 10 sec.

3. `driver.send_ScrollDown(times)` : sending scroll down to the webpage. `times:(int)` decide how many times the command is sent.

4. `driver.send_End(times)` : sending end to the webpage. `times:(int)` decide how many times the command is sent.

5. `driver.send_Enter()` : send enter to the webpage. Takes no argument.

6. `driver.send_Left_Alt()`, `driver.send_Right_Alt()` : are the combination of ←/→ and Alt.

7. `find_element_then_click(by, value, sleep_time, loop_max, response)` : find the required element then send click. the method contains multiple attemps to find the element.
    - by (`selenium.webdriver.common.by.By`) could be By.TEXT, By.XPATH etc.    
    - value (`string`) correspond value of by
    - sleep_time (`float`) waiting time between each attemp, default = 0.5
    - loop_max (`int`) total number of attemps
    - response (`bool`) if `True`, the method returns a `bool` for if the method succeed; `False` return `None`
    

