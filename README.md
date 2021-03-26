<h1>SteamBSD installation on the internet </h1> 
<div class="thumb">
  <figure>
    <a href="https://pypi.org/project/steam-acolyte/"><img src="zico-acolyte.png"></a>
    <figcaption>Ready!</figcaption>
  </figure><!--
  --><figure>
    <a href="https://store.steampowered.com/linux/"><img src="zico-linux.png"></a>
    <figcaption>Ready!</figcaption>
  </figure><!--
  --><figure>
    <a href="https://www.winehq.org/"><img src="zico-wine.png"></a>
    <figcaption>Ready!</figcaption>
  </figure><!--
  --><figure>
    <a href="https://lpros.blogspot.com/p/in-operating-system-steambsd-i-have.html"><img src="https://1.bp.blogspot.com/-K5ZThGhPWNM/YFh8CuPZ49I/AAAAAAAAAkw/JmK2Mmv4pTUdoxHNzDv0Mx_ecZ-Wc0dQgCLcBGAsYHQ/s140/rssl.png"></a>
    <figcaption>Ready!</figcaption>
  </figure>
</div>
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
<br>nvidia - recommended, best choice for linux steam *
<br>amdgpu - not bad for wine steam
<br>radeon - not bad for wine steam
<br>intel - not bad for wine steam
<br>vesa - for test virtual machines
<br>[your_desktop] choose between lxde, lxqt, lumina and plasma
<br>
<br>Only for this internet installer (NOT for ISO IMG) you may choose old driver: nvidia-390, nvidia-340, nvidia-304
<br>
<br>For example:
<br><code>./run bob nvidia plasma </code>
<br><code>./run lee nvidia-390 lxqt </code>
<br><code>./run kim nvidia-340 lumina</code>
<br><code>./run son nvidia-304 lxde</code>
<br><code>./run den amdgpu plasma</code>
<br><code>./run zed radeon lumina</code>
<br><code>./run hanna intel lxqt</code>
<br><code>./run vmuser vesa lxde</code>
<br>
<br>NOTE. If you install on VirtualBox you must choose VMSVGA+128Mb (in virtualbox of course). This is in machine "settings -> display".
<br> 
<br>---
<br>Offline ISO and IMG (fast installation).
<br>Download: https://mega.nz/folder/JgYxmALQ#vR_8PKsr6qL7_xwv39Y2Dw
<br> 
<br>--- SteamBSD © is FREE operating system.
<br>Site: https://lpros.blogspot.com/
<br>E-mail: steambsd@gmail.com
<br><a href="https://lpros.blogspot.com/"><img src="wall.jpg"></a>
<br>File of <a href="https://github.com/steambsd/os/blob/go/LICENSE">license</a>
<br>
<br>How to use MEGA (Attention! You must create new accaunt in commandline):
<br><code>megareg --register --email somename@domain.example --name somename --password 1234</code>
<br><code>megareg --verify vbFFFv7AFM25etzkFXLs9A==:Z7F... https://mega.nz/#confirmciyfWXRGFNcM...</code>
<br><code>megamkdir --username somename@domain.example --password 1234 /Root/test</code>
<br><code>megacopy --username somename@domain.example --password 1234 --local . --remote /Root/yourdir</code>
<br><code>megaget --username somename@domain.example --password 1234 --path . /Root/yourdir/file.tst</code>
<br>
<br>Second command explanation:
<br><code>megareg --verify @stat@ @link@</code>
<br>@stat@ - pass that was returned from megareg, for example vbFFFv7AFM25etzkFXLs9A==:Z7F...
<br>@link@ - is registration link from the 'MEGA Signup' email, for example https://mega.nz/#confirmciyfWXRGFNcM...
