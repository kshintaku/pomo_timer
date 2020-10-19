# Pomodoro Timer

![Screen Shot of Pomo Timer](https://raw.githubusercontent.com/kshintaku/pomo_timer/main/images/ss.png)

I created this timer because I wanted a simple pomodoro timer that I could use while streaming. Having it as it's own window allows me to capture it with OBS without having it take up screen space as other windows can be on top of it and still get captured.

You're welcome to pull the code and use it freely. If you have any suggestions for modifications or improvements I'd love to hear them. I'd like to incorporate a sound file but it wasn't getting packaged with the app installer so I'd have to include additional instructions and a link to any audio I want to use.

## Requirements

- MacOS
- Python3

## Build Instructions

1. Run `pip install requirements.txt`
2. Create an app with `python setup.py py2app`.

## Dev Build Instructions

1. Any changes to the code may require a new `setup.py` file to be created. To do this run `py2applet --make-setup pom_timer.py`
2. Add `'iconfile': './images/pom_timer.icns'` to `setup.py` in the `OPTIONS` field like so:
~~~
OPTIONS = {
    'iconfile': './images/pom_timer.icns'
}
~~~


## Future Improvements

- [ ] Incorporate audio file into build.
- [ ] Create Windows/Linux installer.
- [ ] Address drift issues with timer.
- [ ] Add break tab for 5 min timer.

### Special Thanks

Thank you https://icon-icons.com/ for providing a free icons to use for personal applications.
