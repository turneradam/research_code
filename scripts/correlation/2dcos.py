#!/usr/bin/env python
from scipy import *
from scipy.interpolate import interp1d
from scipy.signal import medfilt2d
from mpl_toolkits.axes_grid1 import make_axes_locatable
from matplotlib.ticker import MaxNLocator
import pylab, sys
import pandas as pd

def label(ax, text, subplot, **kwargs):
    # designate as sync or async
    x1, x2 = ax.get_xlim()
    y1, y2 = ax.get_ylim()
    if 'frac' in kwargs:
       t = ax.text(1.12*(x2-x1) + x1, 0.55*(y2-y1) + y1, text, ha='center', va='center',
            fontdict={'family':'sans-serif', 'size':12, 'weight':'bold'})
       t2 = ax.text(1.12*(x2-x1) + x1, 0.2*(y2-y1) + y1, '%d%%' %
               int(kwargs['frac']+0.5), ha='center', va='center',
            fontdict={'family':'sans-serif', 'size':7})
       t2.set_clip_on(False)
    else:
       t = ax.text(1.12*(x2-x1) + x1, 0.5*(y2-y1) + y1, text, ha='center', va='center',
            fontdict={'family':'sans-serif', 'size':12})
    t.set_clip_on(False)

    # label subplot
    if subS != '':
        x1, x2 = ax_main.get_xlim()
        y1, y2 = ax_main.get_ylim()
        ax_main.text(0.09*(x2-x1)+x1, 0.09*(y2-y1)+y1, subplot, ha='center',
                va='center', fontdict={'size':9, 'weight':'bold'})

def synchronous(dataset1, dataset2):
    phi = zeros([ptsMax1,ptsMax2])
    for i in range(ptsMax1):
        for j in range(ptsMax2):
            phi[i,j] = dot(dataset1[:,i], dataset2[:,j])
    return phi / (m - 1.0)


def asynchronous(dataset1, dataset2):
    psi = zeros([ptsMax1,ptsMax2])
    for i in range(ptsMax1):
        for j in range(ptsMax2):
            psi[i,j] = dot(dataset1[:,i], dot(N, dataset2[:,j]))
    return psi / (m - 1.0)


def pretty2D(dataset):
   # split data into positive and negative sets for plotting contours
   pos_data = zeros([ptsMax1,ptsMax2])
   neg_data = zeros([ptsMax1,ptsMax2])
   someNegData = False
   for i in range(ptsMax1):
      for j in range(ptsMax2):
         if dataset[i,j] > 0:
            pos_data[i,j] = dataset[i,j]
         else:
            someNegData = True
            neg_data[i,j] = abs(dataset[i,j])

   # filtering
   pos_data = medfilt2d(pos_data, kernel_size=(5,5))
   neg_data = medfilt2d(neg_data, kernel_size=(5,5))


   # note: transposing
   extreme = 0.5*max(abs(dataset).flatten())   
   ax_main.contour(pos_data.T, levels, extent=[min(wn2),max(wn2),min(wn1),max(wn1)], origin='lower', colors='r', linewidths=0.5)
   if someNegData:
      ax_main.contour(neg_data.T, levels, extent=[min(wn2),max(wn2),min(wn1),max(wn1)], origin='lower', colors='b', linewidths=0.5)

   ax_main.set_xlabel(xname)
   ax_main.set_ylabel(yname)

   for p in peaks:
      ax_main.axvline(p, color='k', ls='-', lw=0.5)
      ax_main.axhline(p, color='k', ls='-', lw=0.5)

   ax_main.xaxis.set_major_locator(MaxNLocator(5))
   ax_main.yaxis.set_major_locator(MaxNLocator(5))

   if sys.argv[1] == sys.argv[2]:
      ax_main.plot([min(wn),max(wn)], [min(wn),max(wn)], 'k-', lw=0.5)

   divider = make_axes_locatable(ax_main)

   ax_right = divider.append_axes('right', 0)
#   ax_right = divider.append_axes('right', 0.4, pad=0.05, sharey=ax_main)
#   ax_right.fill_betweenx(wn2, 0, ref2, where=ref2<0, facecolor='0.9', lw=0)
#   ax_right.fill_betweenx(wn2, ref2, 0, where=ref2>0, facecolor='0.9', lw=0)
#   ax_right.plot(ref2, wn2, 'k-')
   for p in peaks:
      ax_right.axhline(p, color='k', ls='-', lw=0.5)
   if min(ref2) < 0. and max(ref2) > 0:
      ax_right.axvline(0., color='k', ls='--', lw=0.5, dashes=[2,2])
   pylab.setp(ax_right.get_xticklabels()+ax_right.get_yticklabels(), visible=False)
   pylab.setp(ax_right.get_xticklines()+ax_right.get_yticklines(), visible=False)

   ax_top = divider.append_axes('top', 0)
#   ax_top = divider.append_axes('top', 0.4, pad=0.05, sharex=ax_main)
#   ax_top.fill_between(wn1, 0, ref1, where=ref1<0, facecolor='0.9', lw=0)
#   ax_top.fill_between(wn1, ref1, 0, where=ref1>0, facecolor='0.9', lw=0)
#   ax_top.plot(wn1, ref1, 'k-')
   for p in peaks:
      ax_top.axvline(p, color='k', ls='-', lw=0.5)
   if min(ref1) < 0. and max(ref1) > 0:
      ax_top.axhline(0., color='k', ls='--', lw=0.5, dashes=[2,2])
   pylab.setp(ax_top.get_xticklabels()+ax_top.get_yticklabels(), visible=False)
   pylab.setp(ax_top.get_xticklines()+ax_top.get_yticklines(), visible=False)
   ax_top.set_ylim(0.9*min(ref1), 1.1*max(ref1))

   ax_main.set_xlim(min(wn1),max(wn1))
   ax_main.set_ylim(min(wn2),max(wn2))
   return ax_top

# get ready for beautiful things
pylab.rc('figure', figsize=(6, 3))
pylab.rc('font', size=8)
fig = pylab.figure()
levels = 10

# check out input files and gather some statistics

# first set of spectra
hndl = open(sys.argv[1], 'rt')
set = hndl.readlines()
hndl.close()
wnStart = 0
wnEnd = 999999.
ptsMax1 = 0.
m = len(set)
for file in set:
   wn, absorbance = loadtxt(file.strip(), delimiter=',', unpack=True)

   if wn[0]> wn[-1]:
      wn=wn[::-1]
   if wn[0] > wnStart:
      wnStart = wn[0]
   if wn[-1] < wnEnd:
      wnEnd = wn[-1]
   if len(wn) > ptsMax1:
      ptsMax1 = len(wn)

dataset = []
wn1 = linspace(wnStart, wnEnd, ptsMax1)
for file in set:
   wntemp, abstemp = loadtxt(file.strip(), delimiter=',', unpack=True)

   if wntemp[0]> wntemp[-1]:
      wntemp=wntemp[::-1]
      abstemp=abstemp[::-1]
   f = interp1d(wntemp, abstemp)
   dataset.append(f(wn1))
dataset1 = array(dataset)


# second set of spectra
hndl = open(sys.argv[2], 'rt')
set = hndl.readlines()
hndl.close()
wnStart = 0
wnEnd = 999999.
ptsMax2 = 0.
for file in set:
   wn, absorbance = loadtxt(file.strip(), delimiter=',', unpack=True)

   if wn[0]> wn[-1]:
      wn=wn[::-1]
   if wn[0] > wnStart:
      wnStart = wn[0]
   if wn[-1] < wnEnd:
      wnEnd = wn[-1]
   if len(wn) > ptsMax2:
      ptsMax2 = len(wn)

dataset = []
wn2 = linspace(wnStart, wnEnd, ptsMax2)
for file in set:
   wntemp, abstemp = loadtxt(file.strip(), delimiter=',', unpack=True)

   if wntemp[0]> wntemp[-1]:
      wntemp=wntemp[::-1]
      abstemp=abstemp[::-1]
   f = interp1d(wntemp, abstemp)
   dataset.append(f(wn2))
dataset2 = array(dataset)


# Hilbert-Noda transform
N = zeros([m,m])
for i in range(m):
   for j in range(m):
      if j != i:
         N[i,j] = 1.0/((j - i)*pi)


#calculate the reference spectra (in this case, as the average of all spectra)
ref1 = zeros(ptsMax1)
ref2 = zeros(ptsMax2)
for x in range(m):
   ref1 += dataset1[x,:] / m
for x in range(m):
   ref2 += dataset2[x,:] / m

#subtract the reference spectrum
for x in range(m):
   dataset1[x,:] -= ref1
for x in range(m):
   dataset2[x,:] -= ref2


# axis labels
try:
   hndl = open(sys.argv[3], 'rt')
   settings = hndl.readlines()
   hndl.close()
   xname = settings[0][:-1]
   yname = settings[1][:-1]
   subS = settings[2][:-1]
   subAS = settings[3][:-1]
except:
   xname = 'wavenumber 1'
   yname = 'wavenumber 2'
   subS = ''
   subAS = ''

# peak annotations
try:
   peaks = loadtxt('peaks.txt', unpack=True)
except:
   peaks = []

# synchronous
ax_main = fig.add_subplot(1,2,1)
vals = synchronous(dataset1, dataset2)
ax = pretty2D(vals)
#ax.set_title(sys.argv[1].split('.')[0].upper() + '-' + sys.argv[2].split('.')[0].upper())
#label(ax, '(a)', subS)
#label(ax, '$\Phi$', subS)

# asynchronous
ax_main = fig.add_subplot(1,2,2)
valas = asynchronous(dataset1, dataset2)
ax = pretty2D(valas)

fASS = max(abs(valas.flatten()))/max(abs(vals.flatten()))*100
#label(ax, '(b)', subAS)
#label(ax, '$\Psi$', subAS, frac=fASS)

fig.text(.15, .9, '(a)', horizontalalignment='center',
        verticalalignment='center', transform=ax.transAxes,
            fontdict={'family':'sans-serif', 'size':12})

fig.text(.64, .9, '(b)', horizontalalignment='center',
        verticalalignment='center', transform=ax.transAxes,
            fontdict={'family':'sans-serif', 'size':12})

#fig.tick_params(direction='in')

# save the output
fig.set_tight_layout(True)
mergedName = sys.argv[1].split('.')[0] + '_' + sys.argv[2].split('.')[0] + '.png'
pylab.savefig(mergedName, dpi=1200)

# create csv of sync and async
valsdf = pd.DataFrame(data=vals)
valsdf.to_csv("valsdf.csv")
valasdf = pd.DataFrame(data=valas)
valasdf.to_csv("valasdf.csv")
