--enable-kvm without root
=====

### /etc/udev/rules.d/65-kvm.rules
```bash
KERNEL=="kvm", NAME="%k", GROUP="kvm", MODE="0660"
