#!/usr/bin/env python
# -*- coding: utf-8 -*-

class ServerInfo(object):

  def __init__(self):
    self.local_os = ''
    self.local_kernel = ''
    self.local_hostname = ''
    self.local_distributive = ''
    self.local_architecture = ''

  def to_string(self):
    all_data = "Operation System: " + str(self.local_os) + "\n" "HostName: " + str(self.local_hostname) + "\n" + "Kernel: " + str(self.local_kernel) + "\n" \
               + "Distributive: " + str(self.local_distributive) + "\n" + "Archietecture: " + str(self.local_architecture) + "\n"
    return str(all_data)

  def print_data(self):
    print "Operation System: " + str(self.local_os)
    print "HostName: " + str(self.local_hostname)
    print "Kernel: " + str(self.local_kernel)
    print "Distributive: " + str(self.local_distributive)
    print "Archietecture: " + str(self.local_architecture) + "\n"