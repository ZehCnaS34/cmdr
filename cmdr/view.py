from curses import wrapper
from time import sleep


def wrapped(fn):
    def inner(*args, **kwargs):
        def proxy(stdscr):
            fn(stdscr, *args, **kwargs)
        return wrapper(proxy)
    return inner


@wrapped
def screen(stdscr, project_view):
    stdscr.clear()
    stdscr.nodelay(1)

    while True:
        stdscr.refresh()
        key = stdscr.getch()

        if key >= 0:
            stdscr.addstr(0, 0, '{}'.format(key))

        stdscr.addstr(1, 0, '{}'.format(project_view.render()))

        if key == ord('q'):
            break

        sleep(0.02)
