<h1>SteamBSD installation on the internet </h1>
<br><b>Install FreBSD, reboot PC and login as root:</b>
<br><code>su root</code>
<br><b>Download from git:</b>
<br><code>pkg ins git</code>
<br><code>git clone https://github.com/steambsd/inet</code>
<br><code>cd inet</code>
<br><b>Or download without install git:</b>
<br><code>fetch https://github.com/steambsd/inet/archive/main.zip</code>
<br><code>unzip main.zip</code>
<br><code>cd inet-main</code>
<br>
<br><b>Add permission:</b>
<br><code>chmod +x *</code>
<br> 
<br><b>Finally, run it:</b>
<br><code>./steambsd [your_user] [video_driver] </code>
<br>
<br><b>Where:</b>
<br><b>[your_user]</b> is user created during installation
<br><b>[video_driver]</b> is one of: nvidia, amdgpu, radeon, intel or vesa
<br><b>nvidia</b> - [recommended] best choice for linux steam
<br><b>amdgpu</b> - not bad for wine steam
<br><b>radeon</b> - not bad for wine steam
<br><b>intel</b> - not bad for wine steam
<br><b>vesa</b> - for test virtual machines
<br> 
<br>---
<br>Offline ISO and IMG (fast installation).
<br>Download: https://drive.google.com/drive/folders/18toZCkXbWEp226KgjWZecLe1ad6-FMze
<br> 
<br>---
<br>SteamBSD © is FREE operating system.
<br>Site: http://steambsd.epizy.com
<br>E-mail: light.progres@gmail.com.
