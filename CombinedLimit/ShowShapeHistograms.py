import ROOT

dir = "./DATACARDS_1Dshape/"
file = "simple-shapes-TH1_T2tt_S650N325.root"

def main():
    f = ROOT.TFile.Open(dir+file,"read")
    sig = f.Get("signal")
    sig.SetDirectory(0)
    backg = f.Get("background")
    backg.SetDirectory(0)
    
    canv = ROOT.TCanvas()
    ROOT.gStyle.SetOptStat(0)
    canv.SetLogy()
    backg.GetYaxis().SetTitle("Entries")
    backg.GetXaxis().SetTitle("m_{T2}(ll) (GeV)")
    backg.GetYaxis().SetTitleSize(0.042)
    backg.GetXaxis().SetTitleSize(0.042)
    backg.SetLineColor(ROOT.kBlack)
    sig.SetLineColor(ROOT.kRed)
    backg.SetLineWidth(3)
    sig.SetLineWidth(3)
    l = ROOT.TLegend(0.7,0.7,0.9,0.9)
    l.SetFillColor(0)
    l.SetShadowColor(ROOT.kWhite)
    l.SetBorderSize(1)
    l.AddEntry(backg,"background")
    l.AddEntry(sig, "signal")
    backg.Draw("hist")
    sig.Draw("histSAME")
    l.Draw("same")
    canv.SaveAs("./ShowShapeHistograms.png")

if __name__ == "__main__":
    main()
