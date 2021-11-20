__all__ = ['Heartbeat']

import enum
import threading
import time

import ipywidgets.widgets as widgets
import traitlets
from IPython.display import display
from traitlets.config.configurable import Configurable


class Heartbeat(Configurable):
    class Status(enum.Enum):
        dead = 0
        alive = 1

    status = traitlets.UseEnum(Status, default_value=Status.dead)
    running = traitlets.Bool(default_value=False)
    
    # config
    period = traitlets.Float(default_value=0.5).tag(config=True)

    def __init__(self, observable_name, observable_heartbeat: float, *args, **kwargs):
        super(Heartbeat, self).__init__(*args,
                                        **kwargs)  # initializes traitlets

        self._period_slider = widgets.FloatSlider(description=observable_name, min=0.01, max=5.0, step=0.01, value=observable_heartbeat)
        traitlets.dlink((self._period_slider, 'value'), (self, 'period'))
        self.pulseout = widgets.FloatText(value=time.time())
        self.pulsein = widgets.FloatText(value=time.time())
        self.link = widgets.jsdlink((self.pulseout, 'value'),
                                    (self.pulsein, 'value'))
        self.observe(self.handle_heartbeat_status, names='status')
        self._name = observable_name
        self.start()

    def display_slider(self):
        display(self._period_slider, self.pulseout)

    def handle_heartbeat_status(self, change):
        if change['new'] == Heartbeat.Status.dead:
            self.stop()

    def _run(self):
        while True:
            if not self.running:
                break
            if self.pulseout.value - self.pulsein.value >= self.period:
                self.status = Heartbeat.Status.dead
            else:
                self.status = Heartbeat.Status.alive
            self.pulseout.value = time.time()
            time.sleep(self.period)

    def start(self):
        if self.running:
            return
        self.running = True
        self.thread = threading.Thread(target=self._run)
        self.thread.start()

    def stop(self):
        self.running = False
        print(f"{self._name} stopped")

