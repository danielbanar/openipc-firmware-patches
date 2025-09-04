>### OpenIPC FPV over 4G/LTE (Masina)
>
>This branch includes my patches such as: wireguard support, 4G/LTE modem drivers, and the masinaclient.
>
>### Supported devieces
>##### SoC
>- SSC30KQ
>- SSC338Q
>##### Modems
>- SIMCOM7600 series (SIM7600G-H, ...)
>- Quectel EC25 series (EG25, EC25-EUX, ...)
>- Other modems such as Huawei E3372 should be supported but not tested
>### Configuration
>##### WireGuard
>You will need to replace the following placeholders with your actual values in `general/overlay/root/wireguard`
>
>- `PrivateKey`
>- `PresharedKey`
>- `PublicKey`
>- Domain or public IP address
>- Virtual client IP'
>
>If you are using PiVPN, you can find these values in your client configuration file, typically located at:
>
>```
>~/home/<user>/configs/<client.conf>
>```
>##### Modem
>To set your modem set this env variable
>`fw_setenv wlandev ec25`
>All available modem names are in: `general/overlay/etc/wireless/modem`
>
>Before that you might need to change the modes, I recommend doing this on your PC, plug the modem use the serial interfaces for AT commands (usually /dev/ttyUSB2) and set the mode:
>- EC25 ECM Mode`AT+QCFG="usbnet",1`
>- EC25 RNDIS Mode`AT+QCFG="usbnet",3`
>
>##### Masina Client (control over 4G/LTE)
> This is my app that allows you to use serial port on your camera soc as a ELRS/CRSF receiver, so you can control it over internet and receive telemetry aswell, this requires running the server app on your GS (only Windows, Linux version not public).
>You can also use Dual control ELRS and Masina with the ability to switch between them on the fly (If you lose ELRS link, switch to Masina) this way if you lose data completelly you can still receive GPS coordinates as telemetry from the receiver if you get close to it. This Requires extra hardware (TS5A23157 MUX board) that can be switched with a GPIO pin on your cameras SoC.
>If you want to use regualar ELRS receiver instead, you can disable this in `root/masina` by setting `enabled=false`
>
>###### Config
>Config file stored as`root/masina`:
>```GROUND_IP=<GS Virtual IP>
>LOCAL_TIMEOUT=<ms (switch to ELRS instead of Masina if no data received for x miliseconds, does nothing when not using dual control)>
>FAILSAFE_TIMEOUT=<ms (Failsafe - Land or RTH after no data for x miliseconds, recommended: 5000)>
>STABILIZE_TIMEOUT=<ms (Stabilize/Hover - Angle mode with constant throttle after no data for x miliseconds, recommended: 250)>
>ELRS_SWITCH_PIN=<DUAL control switch GPIO pin>
>HOVER_VALUE=<value between 1000-2000 (Throttle value when Stabilize/Hover is active)>
```



---

![OpenIPC logo][logo]

## Alternative open firmware for your IP camera
_(based on Buildroot)_

[![Telegram](https://openipc.org/images/telegram_button.svg)][telegram]


OpenIPC is a rapidly developing open source alternative [firmware][firmware] for 
popular IP cameras from an [open community](https://opencollective.com/openipc).

Historically, OpenIPC [firmware][firmware] only supported SoC manufactured by 
HiSilicon, but as the development continues, the list of supported processors
expands. Today, it also includes chips from _Ambarella_, _Anyka_, _Fullhan_, _Goke_,
_GrainMedia_, _Ingenic_, _MStar_, _Novatek_, _SigmaStar_, _XiongMai_, and is 
expected to grow further.

More information about the [project][project] is available in our [website][website]
and on the [wiki][wiki].

## Support

OpenIPC offers two levels of support.

- Free support through the community (via [chat][telegram]).
- Paid commercial support (from the team of developers).

Please consider subscribing for paid commercial support if you intend to use our product for business.
As a paid customer, you will get technical support and maintenance services directly from our skilled team.
Your bug reports and feature requests will get prioritized attention and expedited solutions. It's a win-win
strategy for both parties, that would contribute to the stability your business, and help core developers
to work on the project full-time.

If you have any specific questions concerning our project, feel free to [contact us](mailto:dev@openipc.org).


## Participating and Contribution

If you like what we do, and willing to intensify the development, please consider participating.

You can improve existing code and send us patches. You can add new features missing from our code.

You can help us to write a better documentation, proofread and correct our websites.

You can just donate some money to cover the cost of development and long-term maintaining of what we believe
is going to be the most stable, flexible, and open IP Network Camera Framework for users like yourself.

You can make a financial contribution to the project at [Open Collective][contribution].

Thank you.

<p align="center">
<a href="https://opencollective.com/openipc/contribute/backer-14335/checkout" target="_blank"><img src="https://opencollective.com/webpack/donate/button@2x.png?color=blue" width="250" alt="Open Collective donate button"></a>
</p>

[chat]: https://openipc.org/our-channels
[contribution]: https://opencollective.com/openipc/contribute/backer-14335/checkout


[firmware]: https://github.com/openipc/firmware
[logo]: https://openipc.org/assets/openipc-logo-black.svg
[mit]: https://opensource.org/license/mit
[opencollective]: https://opencollective.com/openipc
[paypal]: https://www.paypal.com/donate/?hosted_button_id=C6F7UJLA58MBS
[project]: https://github.com/openipc
[telegram]: https://openipc.org/our-channels
[website]: https://openipc.org
[wiki]: https://github.com/openipc/wiki
