import ROOT

def TwoD(TwoDhist):

    nbinsX = TwoDhist.GetNbinsX()
    nbinsY = TwoDhist.GetNbinsY()

    hout = ROOT.TH1D("","",nbinsX*nbinsY,0,nbinsX*nbinsY)
    l=1
    for i in range(1,nbinsX+1):
        for j in range(1,nbinsY+1):
            bin = TwoDhist.GetBin(i,j)
            hout.SetBinContent(l,TwoDhist.GetBinContent(bin))
            l+=1
    return hout

def ThreeD(ThreeDhist):
    
    nbinsX = ThreeDhist.GetNbinsX()
    nbinsY = ThreeDhist.GetNbinsY()
    nbinsZ = ThreeDhist.GetNbinsZ()

    hout = ROOT.TH1D("","",nbinsX*nbinsY*nbinsZ,0,nbinsX*nbinsY*nbinsZ)
    l=1
    for i in range(1,nbinsX+1):
        for j in range(1,nbinsY+1):
            for k in range(1,nbinsZ+1):
                bin = ThreeDhist.GetBin(i,j,k)
                hout.SetBinContent(l,ThreeDhist.GetBinContent(bin))
                l+=1
    return hout
