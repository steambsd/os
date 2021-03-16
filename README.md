<h1>SteamBSD installation on the internet </h1>
<br>Install FreeBSD, reboot PC and login as root:
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
<br><code>chmod +x run</code>
<br> 
<br>Finally, run it:
<br><code>./run [your_user] [video_driver] [your_desktop]</code>
<br>Or run it without paramtrs (default user "admin" with pass "0000", driver "nvidia" and desktop "lxqt"):
<br><code>./run</code>
<br>
<br>Where:
<br>[your_user] is user created during installation 
<br>If the user does not exist, the script will add it automatically with the password "0000", you can change the password after installation:
<br><code>passwd [your_user]</code>
<br>[video_driver] is one of: nvidia, amdgpu, radeon, intel or vesa
<br>nvidia - recommended, best choice for linux steam *
<br>amdgpu - not bad for wine steam
<br>radeon - not bad for wine steam
<br>intel - not bad for wine steam
<br>vesa - for test virtual machines
<br>[your_desktop] choose between lxde, lxqt and kde
<br>
<br>Only for this internet installer (NOT for ISO IMG) you may choose old driver: nvidia-390, nvidia-340, nvidia-304
<br>
<br>For example:
<br><code>./run bob nvidia kde </code>
<br><code>./run lee nvidia-390 lxde </code>
<br><code>./run kim nvidia-340 kde</code>
<br><code>./run son nvidia-304 lxde</code>
<br><code>./run den amdgpu kde</code>
<br><code>./run zed radeon lxde</code>
<br><code>./run hanna intel kde</code>
<br><code>./run vmuser vesa lxde</code>
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
