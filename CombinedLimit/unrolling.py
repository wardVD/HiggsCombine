import ROOT

def TwoD(TwoDhist):

    nbinsX = TwoDhist.GetNbinsX()+1 #include overflow
    nbinsY = TwoDhist.GetNbinsY()+1 #include overflow
    #XrangeMin = TwoDhist.GetXaxis().GetXmin()
    #XrangeMax = TwoDhist.GetXaxis().GetXmax()
    #YrangeMin = TwoDhist.GetYaxis().GetXmin()
    #YrangeMax = TwoDhist.GetYaxis().GetXmax()

    hout = ROOT.TH1F("","",nbinsX*nbinsY,0,nbinsX*nbinsY)
    l=1
    for j in range(1,nbinsY+1):
        for i in range(1,nbinsX+1):
            bin = TwoDhist.GetBin(i,j)
            hout.SetBinContent(l,TwoDhist.GetBinContent(bin))
            l+=1
    return hout

def ThreeD(ThreeDhist):
    
    nbinsX = ThreeDhist.GetNbinsX()+1 #include overflow
    nbinsY = ThreeDhist.GetNbinsY()+1 #include overflow
    nbinsZ = ThreeDhist.GetNbinsZ()+1 #include overflow

    hout = ROOT.TH1F("","",nbinsX*nbinsY*nbinsZ,0,nbinsX*nbinsY*nbinsZ)
    l=1
    for k in range(1,nbinsZ+1):
        for j in range(1,nbinsY+1):
            for i in range(1,nbinsX+1):
                bin = ThreeDhist.GetBin(i,j,k)
                hout.SetBinContent(l,ThreeDhist.GetBinContent(bin))
                l+=1
    return hout
