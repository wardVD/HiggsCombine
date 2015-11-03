import ROOT

dir = "./DATACARDS_3Dshape/"
#dir = './stuff_met80_metsig5_njets2ormore_bnjets1ormore_dphi0.25/DATACARDS_3Dshape/'
file = "simple-shapes-TH3_SMS_T2tt_2J_mStop650_mLSP325.root"

def main():
    f = ROOT.TFile.Open(dir+file,"read")
    sig = f.Get("signal")
    sig.SetDirectory(0)
    sigUp = f.Get("signal_sigmaUp") 
    sigUp.SetDirectory(0)
    sigDown = f.Get("signal_sigmaDown")
    sigDown.SetDirectory(0)
    backg = f.Get("background")
    backg.SetDirectory(0)
    backgUp = f.Get("background_alphaUp")
    backgUp.SetDirectory(0)
    backgDown = f.Get("background_alphaDown")
    backgDown.SetDirectory(0)
    
    canv = ROOT.TCanvas()
    ROOT.gStyle.SetOptStat(0)
    canv.SetLogy()
    backgUp.GetYaxis().SetTitle("Entries")
    backgUp.GetXaxis().SetTitle("m_{T2}(ll) (GeV)")
    backgUp.GetYaxis().SetTitleSize(0.042)
    backgUp.GetXaxis().SetTitleSize(0.042)
    backg.SetLineColor(ROOT.kBlack)
    sig.SetLineColor(ROOT.kRed)
    backgUp.SetLineColor(ROOT.kBlue)
    backgDown.SetLineColor(ROOT.kBlue)
    sigUp.SetLineColor(ROOT.kOrange)
    sigDown.SetLineColor(ROOT.kOrange)
    backg.SetLineWidth(3)
    sig.SetLineWidth(3)
    l = ROOT.TLegend(0.7,0.7,0.9,0.9)
    l.SetFillColor(0)
    l.SetShadowColor(ROOT.kWhite)
    l.SetBorderSize(1)
    l.AddEntry(backg,"background","l")
    l.AddEntry(backgUp,"error bkg","l")
    l.AddEntry(sig, "signal","l")
    l.AddEntry(sigUp, "error signal","l")
    backgUp.Draw("hist")
    backg.Draw("histSAME")
    backgDown.Draw("histsame")
    sigUp.Draw("histsame")
    sig.Draw("histSAME")
    sigDown.Draw("histsame")
    l.Draw("same")
    canv.SaveAs("./ShowShapeHistograms.png")

if __name__ == "__main__":
    main()

