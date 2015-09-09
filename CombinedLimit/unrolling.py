import ROOT

def TwoD(TwoDhist):

    nbinsX = TwoDhist.GetNbinsX()+2 #include underflow/overflow
    nbinsY = TwoDhist.GetNbinsY()+2 #include underflow/overflow
    #XrangeMin = TwoDhist.GetXaxis().GetXmin()
    #XrangeMax = TwoDhist.GetXaxis().GetXmax()
    #YrangeMin = TwoDhist.GetYaxis().GetXmin()
    #YrangeMax = TwoDhist.GetYaxis().GetXmax()

    hout = ROOT.TH1F("","",nbinsX*nbinsY,0,nbinsX*nbinsY)
    for j in range(nbinsY):
        for i in range(nbinsX):
            bin = TwoDhist.GetBin(i,j)
            hout.SetBinContent(bin,TwoDhist.GetBinContent(bin))
    return hout

def ThreeD(ThreeDhist):
    
    nbinsX = ThreeDhist.GetNbinsX()+2 #include underflow/overflow
    nbinsY = ThreeDhist.GetNbinsY()+2 #include underflow/overflow
    nbinsZ = ThreeDhist.GetNbinsZ()+2 #include underflow/overflow

    hout = ROOT.TH1F("","",nbinsX*nbinsY*nbinsZ,0,nbinsX*nbinsY*nbinsZ)
    for k in range(nbinsZ):
        for j in range(nbinsY):
            for i in range(nbinsX):
                bin = ThreeDhist.GetBin(i,j,k)
                hout.SetBinContent(bin,ThreeDhist.GetBinContent(bin))
    return hout
