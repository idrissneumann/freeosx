# Free command for mac

## Git repo

* Main repo: https://gitlab.comwork.io/oss/freeosx
* Github mirror backup: https://github.com/idrissneumann/freeosx
* Gitlab mirror backup: https://gitlab.com/ineumann/freeosx

## How to install it

You can add install with the following procedure:


```shell
$ git clone https://gitlab.comwork.io/oss/freeosx
$ sudo ln -s ${HOME}/freeosx/free.py /usr/local/bin/free
```

N.B: Be sure that the `/usr/local/bin/free` is in your `$PATH` variable and exists. Or else:

```shell
sudo mkdir -p /usr/local/bin
echo "export PATH=\"${PATH}:/usr/local/bin/\" >> ~/.bash_profile"
```

Then enjoy it:

```shell
free
```

## Credit

This script is based on this answer from "drfrogsplat" on StackOverflow: https://apple.stackexchange.com/a/4296/61214
