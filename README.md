>### GK7205V300 + IMX335 FPS Patch Instructions
>
>This patch comes with a modified driver from tipoman's repository: https://github.com/tipoman9/imx335_modes.
>
>I played with the settings a bit more to get these:
>```
>2048x1536@30fps 4:3, full sensor
>1920x1440@39fps 4:3, full sensor
>1920x1080@53fps 16:9, top cropped
>1920x1080@54fps 16:9, cropped in
>1600x900@75fps 16:9, cropped in
>1280x720@88fps 16:9, cropped in
>2304x1296@37fps 16:9, top cropped
>1856x1044@59fps 16:9, cropped in
>```
>If you want to apply this to an already existing OpenIPC firmware repository, you can do so by using the included `gk7205v300_imx335-fps.patch` file:
>
>1. Copy the `gk7205v300_imx335-fps.patch` file into your local OpenIPC firmware folder.
>2. Run:
>   ```bash
>   git apply gk7205v300_imx335-fps.patch
>   ```
>
>#### Configuration Notes
>
>I included a default majestic.yaml configuration due to elements in the ISP tab of Majestic missing for some reason.
>
>In order to get each mode working you need to set these values:
>
>- In `/etc/sensors/imx335_fps.ini`: `DevRect_w`, `DevRect_h`, `Isp_FrameRate`
>- Majestic: `Resolution`, `Framerate`
>
>| Majestic resolution   | Aspect Ratio   | Actual framerate   |   DevRect_w |   DevRect_h |   Isp_FrameRate & Majestic framerate | Cropped        |
>|:----------------------|:---------------|:-------------------|------------:|------------:|-------------------------------------:|:---------------|
>| 2048x1536             | 4:3            | 30fps              |        2592 |        1944 |              35                      |                |
>| 1920x1440             | 4:3            | 39fps              |        2592 |        1944 |              45                      |                |
>| 1920x1080             | 16:9           | 53fps              |        2592 |        1520 |              55                      | Yes (top only) |
>| 1920x1080             | 16:9           | 54fps              |        1920 |        1080 |              55                      | Yes            |
>| 1600x900              | 16:9           | 75fps              |        1920 |        1080 |              77                      | Yes            |
>| 1280x720              | 16:9           | 88fps              |        1920 |        1080 |              90                      | Yes            |
>| 2304x1296             | 16:9           | 37fps              |        2560 |        1944 |              38                      | Yes (top only) |
>| 1856x1044             | 16:9           | 59fps              |        1920 |        1080 |              60                      | Yes            |
>
>#### Caution
> With these increased framerates the camera starts to heat up more, make sure its not running hot and maybe put on a heatsink.
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
