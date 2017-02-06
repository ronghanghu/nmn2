#!/usr/bin/env python2

import numpy as np
import os
import scipy

VIS_DIR = "vis"

class Visualizer:
    def __init__(self):
        self.active = False

    def begin(self, dest, max_entries):
        self.lines = []
        self.active = True
        self.max_entries = max_entries
        self.next_entry = 0

        self.dest_dir = os.path.join(VIS_DIR, dest)
        if not os.path.exists(self.dest_dir):
            os.mkdir(self.dest_dir)

    def reset(self):
        self.next_entry = 0
        self.active = True

    def end(self):
        self.active = False

        with open(os.path.join(self.dest_dir, "index.html"), "w") as vis_file:
            #print >>vis_file, "<html><head><link rel='stylesheet' href='style.css'></head><body><table>"
            print("<html><head>", file=vis_file)
            print("<link rel='stylesheet' href='../style.css' />", file=vis_file)
            print("</head><body><table>", file=vis_file)
            for line in self.lines:
                print("  <tr>", file=vis_file)
                for field in line:
                    print("    <td>", end=' ', file=vis_file)
                    print(field, end=' ', file=vis_file)
                    print("</td>", file=vis_file)
                print("  </tr>", file=vis_file)
            print("</table></body></html>", file=vis_file)

    def show(self, data):
        if not self.active:
            return
        table_data = []
        for i_field, field in enumerate(data):
            if isinstance(field, np.ndarray):
                filename = "%d_%d.jpg" % (self.next_entry, i_field)
                filepath = os.path.join(self.dest_dir, filename)
                scipy.misc.imsave(filepath, field)
                table_data.append("<img src='%s' />" % filename)
            else:
                table_data.append(str(field))

        self.lines.append(table_data)
        self.next_entry += 1
        if self.next_entry >= self.max_entries:
            self.active = False

visualizer = Visualizer()
