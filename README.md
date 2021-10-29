# GHAutoknit - Bridging Grasshopper and Autoknit

A prototypical bridge between Rhino / Grasshopper and [Autoknit](https://github.com/textiles-lab/autoknit).

**WARNING: This code is unfinished. I never completed it because I moved on to another approach!**

## However, it is actually possible to use this...

- This piece of software ships with a pre-built release of autoknit.
- If you want to run using your own, previously compiled version of autoknit, 
you need to set the ``_AK_RAW_PATH_`` variable in ``ghautoknit/Environment.py``
to the folder where your ``interface.exe`` is located.
- With everything set up, it should be possible to run ``Examples/211029_GHAutoknit_Example.gh``.

## Installation

### 1. Download release files

- Go to [releases](https://github.com/fstwn/ghautoknit/releases) and download the newest release
- Right click onto the zip archive and go to **Properties**
- If the text *This file came from another computer [...]* is displayed click on **Unblock**!
- **If you don't do this, you will have to unblock _EVERY_ file in the folder later!**
- Unzip the downloaded archive. You should get two folders: `modules` and `GHAutoknit`.

### 2. Install python modules

- Open the scripts folder of Rhino 7
  - On **Windows**:
  `C:\Users\%USERNAME%\AppData\Roaming\McNeel\Rhinoceros\7.0\scripts`

  - On **Mac OSX**:
  `~/Library/Application Support/McNeel/Rhinoceros/7.0/scripts`
- Move all the Content from inside the `modules` directory to this scripts folder.

### 3. OPTIONAL: Set ``_AK_RAW_PATH_`` variable

- If you want to run using your own, previously compiled instance of autoknit,
you need to set the ``_AK_RAW_PATH_`` variable in ``ghautoknit/Environment.py``
to the folder where your ``interface.exe`` is located.

### 4. Install GHAutoknit UserObjects

- Navigate to the Grasshopper UserObjects folder
  - On **Windows**:
  `C:\Users\%USERNAME%\AppData\Roaming\Grasshopper\UserObjects`

  - On **Mac OSX**:
  `~/Library/Application Support/McNeel/Rhinoceros/6.0/scripts`

  - *Alternative:* Open Rhino & Grasshopper and in the Grasshopper Window click on
  `File` > `Special Folders` > `User Object Folder`

- Move the whole `GHAutoknit` directory to the UserObjects folder.

### 5. Restart Rhino & Grasshopper

- If Rhino was running during the installation process, you'll have to restart it for the changes to take effect!

## Licensing

- Original code is licensed under the MIT License.
- Autoknit is placed in the public domain. This piece of software ships with a
pre-built release of autoknit, please see ``modules/autoknit-windows-v0.1/README.md`` for details.