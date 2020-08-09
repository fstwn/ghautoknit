# GHAutoknit - Bridging Grasshopper and Autoknit

A prototypical bridge between Rhino / Grasshopper and [Autoknit](https://github.com/textiles-lab/autoknit).

**WARNING: This code is unfinished. I never completed it because I moved on to another approach!**

## However, it is actually possible to use this...
- You need a compiled version of Autoknit.
- You need to set the ``_AK_RAW_PATH_`` variable in ``ghautoknit/Environment.py`` to the folder where your ``interface.exe`` is located.
- With everything set up, it should be possible to run ``Examples/GHAutoknit.gh``.

## Installation

### 1. Download release files

- Go to [releases](https://github.com/fstwn/ghautoknit/releases) and download the newest release
- Unzip the downloaded archive. You should get two folders: `modules` and `GHAutoknit`.

### 2. Install python modules

- Open the scripts folder of Rhino 6
  - On **Windows**:
  `C:\Users\%USERNAME%\AppData\Roaming\McNeel\Rhinoceros\6.0\scripts`

  - On **Mac OSX**:
  `~/Library/Application Support/McNeel/Rhinoceros/6.0/scripts`
- Move all the Content from inside the `modules` directory to this scripts folder.

### 3. Set ``_AK_RAW_PATH_`` variable

- You need to set the ``_AK_RAW_PATH_`` variable in ``ghautoknit/Environment.py`` to the folder where your ``interface.exe`` is located.

### 4. Install Cockatoo UserObjects

- Navigate to the Grasshopper UserObjects folder
  - On **Windows**:
  `C:\Users\%USERNAME%\AppData\Roaming\Grasshopper\UserObjects`

  - On **Mac OSX**:
  `~/Library/Application Support/McNeel/Rhinoceros/6.0/scripts`

  - *Alternative:* Open Rhino & Grasshopper and in the Grasshopper Window click on
  `File` > `Special Folders` > `User Object Folder`

- Move the whole `GHAutoknit` directory to the UserObjects folder.

### 5. Unblock the new UserObjects!

- Go into the `GHAutoknit` folder inside Grasshoppers UserObjects folder
- Right click onto the first UserObject and go to **Properties**
- If the text *This file came from another computer [...]* is displayed click on **Unblock**!
- **Unfortunately you have to do this for _EVERY_ UserObject in the folder!**

### 6. Restart Rhino & Grasshopper

- If Rhino was running during the installation process, you'll have to restart it for the changes to take effect!
