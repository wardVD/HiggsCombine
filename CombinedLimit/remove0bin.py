import ROOT


def iszerobin(hist):
    nbins = hist.GetNbinsX()
    zerobin = False
    for i in range(1,nbins+1):
        if hist.GetBinContent(i) <= 0.: 
            zerobin = True
            break
    return [zerobin,i]
        

def newhistogram(hist):
    nbins = hist.GetNbinsX()
    if hist.iszerobin[0]:
        newhist = ROOT.TH1F("","",nbins-1)
        for i in range(1,hist.iszerobin[1]):
            newhist.SetBinContent(i,hist.GetBincontent(i))
        for i in range(hist.iszerobin[1]+1,nbins+1):
            newhist.SetBinContent(i,hist.GetBinContent(i)+1)
        newhist = newhistogram(newhist)
    else:
        return hist
            
        
