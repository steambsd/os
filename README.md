<h1>SteamBSD installation on the internet (develop) </h1> 
<br>Install FreeBSD, reboot PC and login as root:
<br><code>su root</code>
<br>
<br>Download from git:
<br><code>pkg ins git</code>
<br><code>git clone https://github.com/steambsd/os</code>
<br><code>cd os</code>
<br>Or download without install git:
<br><code>fetch https://github.com/steambsd/os/archive/go.zip</code>
<br><code>unzip go.zip</code>
<br><code>cd os-go</code>
<br>
<br>Add permission:
<br><code>chmod +x run</code>
<br> 
<br>Finally, run it:
<br><code>./run [your_user] [video_driver] [your_desktop]</code>
<br>Or run it without paramtrs (default user "admin" with pass "0000", driver "nvidia" and desktop "lumina"):
<br><code>./run</code>
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
<br>[your_desktop] choose between lxde, lxqt, lumina and plasma
<br>
<br>Only for this internet installer (NOT for ISO IMG) you may choose old driver: nvidia-390, nvidia-340, nvidia-304
<br>
<br>For example:
<br><code>./run ash nvidia lumina </code>
<br><code>./run bob nvidia plasma </code>
<br><code>./run lee nvidia-390 lxqt </code>
<br><code>./run kim nvidia-340 lumina</code>
<br><code>./run son nvidia-304 lxde</code>
<br><code>./run den amdgpu plasma</code>
<br><code>./run zed radeon lumina</code>
<br><code>./run hanna intel lxqt</code>
<br><code>./run vmuser vesa lxde</code>
<br>
<br>NOTE1. If you install on VirtualBox you must choose VMSVGA+128Mb (in virtualbox of course). This is in machine "settings -> display".
<br>NOTE2. If you install via ISO disk of FreeBSD and internet - you need synchronize rc.conf (see "run" script). Because chrome and steam may work unstable.
<br> 
<br>--- SteamBSD © is FREE operating system.
<br>Site: https://lpros.blogspot.com/
<br>E-mail: steambsd@gmail.com
<img src="wall.jpg" alt="wall">
<img src="wall2.jpg" alt="wall">
