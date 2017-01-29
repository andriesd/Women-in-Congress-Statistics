women = read.csv('final_data.csv')
women.lm = lm(GenderVar~PercentWomen+PartyVar, data=women)
plot(women.lm)
summary(women.lm)

library(lmtest)
bptest(women.lm)

women_with_regions = read.csv('final_wRegions.csv')
with_regions.lm = lm(GenderVar~PercentWomen+PartyVar+X_regNewEngland+X_regMidAtlantic+X_regENCentral+X_regWNCentral
                +X_regSouthAtlantic+X_regESCentral+X_regWSCentral+X_regMountainWest+X_regPacific, 
                data=women_with_regions)
summary(with_regions.lm)

women = read.csv('womenReg2.csv')
ne.lm = lm(GenderVar ~ PercentWomen + PartyVar + PercentWomen*PartyVar, Northeast == 1, data = women)
summary(ne.lm)

all.lm = lm(GenderVar ~ PercentWomen + PartyVar + Northeast + Midwest + West, data = women)
summary(all.lm)

urb = lm(GenderVar ~ PercentWomen + PartyVar + PerUrban, data = women)
summary(urb)

# interact with urban

urb_interaction = lm(GenderVar ~ PercentWomen + PartyVar + PerUrban + 
                       PercentWomen*PerUrban + PartyVar*PerUrban, data = women)
summary(urb_interaction)

full_interaction = lm(GenderVar ~ PercentWomen + PartyVar + PartyVar*PercentWomen + Northeast + 
                        Midwest + West + Northeast*PercentWomen + Midwest*PercentWomen + 
                        West*PercentWomen + Northeast*PartyVar + Midwest*PartyVar + West*PartyVar + 
                        Northeast*PartyVar*PercentWomen + Midwest*PartyVar*PercentWomen + 
                        West*PartyVar*PercentWomen, data=women)
summary(full_interaction)

urb_effect = lm(formula = GenderVar ~ PercentWomen + PartyVar + PerUrban +
                Midwest * PerUrban + Northeast * PerUrban + West * PerUrban, data = women)
summary(urb_effect)

base = lm(GenderVar ~ PercentWomen + PartyVar, data=women)
summary(base)
