import ROOT, os
import numpy as np

dir = './histograms_ward_10fb_met40_metsig0_njets2ormore_bnjets1ormore_dphi0.25_DY_HT/'
#dir = 'histograms_ward_10fb_met140_metsig8_njets2ormore_bnjets1ormore_dphi0.25_DY_HT/'

samples = os.listdir(dir)

for sample in samples:
    f = ROOT.TFile.Open(dir+sample,"read")
    hist = f.Get("h1_mt2llcounting_mt2llcut_100")
    #hist = f.Get("h1_mt2ll")
    hist.SetDirectory(0)
    nbins = hist.GetNbinsX()
    print sample
    for i in range(nbins):
        print str(i) + ": " + str(round(hist.GetBinContent(i+1),2)) + "+-" + str(round(hist.GetBinError(i+1),2))
    a = np.zeros(1,dtype=float)
    print "Total:", round(hist.IntegralAndError(1,3,a),2), "+-", round(a[0],2)
    print "-------------"    
