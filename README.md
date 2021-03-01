<h1>SteamBSD installation on the internet </h1>
<br>Install FreeBSD (with kernel-dbg, lib32), reboot PC and login as root:
<br><code>su root</code>
<br>Download from git:
<br><code>pkg ins git</code>
<br><code>git clone https://github.com/steambsd/inet</code>
<br><code>cd inet</code>
<br>Or download without install git:
<br><code>fetch https://github.com/steambsd/inet/archive/main.zip</code>
<br><code>unzip main.zip</code>
<br><code>cd inet-main</code>
<br>
<br>Add permission:
<br><code>chmod +x steambsd</code>
<br> 
<br>Finally, run it:
<br><code>./steambsd [your_user] [video_driver] </code>
<br>Or run it without paramtrs (default user "admin" with pass "0000" and driver "nvidia"):
<br><code>./steambsd</code>
<br>
<br>Where:
<br>[your_user] is user created during installation 
<br>If the user does not exist, the script will add it automatically with the password "0000", you can change the password after installation:
<br><code>passwd [your_user]</code>
<br>[video_driver] is one of: nvidia, amdgpu, radeon, intel or vesa
<br>nvidia - recommended, best choice for linux steam
<br>amdgpu - not bad for wine steam
<br>radeon - not bad for wine steam
<br>intel - not bad for wine steam
<br>vesa - for test virtual machines
<br>
<br>For example:
<br><code>./steambsd bob nvidia </code>
<br><code>./steambsd den amdgpu </code>
<br><code>./steambsd zed radeon </code>
<br><code>./steambsd hanna intel </code>
<br><code>./steambsd vmuser vesa </code>
<br> 
<br>---
<br>Offline ISO and IMG (fast installation).
<br>Download: https://drive.google.com/drive/folders/18toZCkXbWEp226KgjWZecLe1ad6-FMze
<br> 
<br>---
<br>SteamBSD © is FREE operating system.
<br>YouTube: SteamBSD (https://www.youtube.com/channel/UC8wwRY8yGWiJ-bIQlK0wvUA)
<br>Site: http://steambsd.epizy.com
<br>E-mail: light.progres@gmail.com.
