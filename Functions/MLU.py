#######################
## get child's MLU ###
#######################

def CHI (file):
    removelist = ['\t', '\r']

    with open(file,'r') as f:
        text = f.read()
        for item in removelist:
            text = text.replace(item, '')
        text = text.split('\n')

        # make a list with only the POS lines from the transcript
        utt = []
        for s, val in enumerate(text):
            if val.startswith('*CHI'):
                m = str(text[s+1])
                m = m[5:]
                utt.append(m)

        morphs = []
        mPL = []
        mPOSS = []
        mPAST = []
        mPROG = []
        mPERF = []
        mTHIRDSING = []
        mCOMP1 = []
        mCOMP2 = []
        mSUPER1 = []
        mSUPER2 = []
        mADVR1 = []
        mADVR2 = []
        mAGT = []

        for s in utt:
            base = s.count('|')
            PL = s.count('-PL')
            POSS = s.count('POSS')
            PAST = s.count('&PAST')
            PROG = s.count('-PROG')
            PERF = s.count('&PERF')
            THIRDSING = s.count('&3S')
            COMP1 = s.count('-CP')
            COMP2 = s.count('&CP')
            SUPER1 = s.count('-SP')
            SUPER2 = s.count('&SP')
            ADVR1 = s.count('-ADVR')
            ADVR2 = s.count('LY')
            AGT = s.count('-AGT')


            m = base + PL + POSS + PAST + PROG + PERF + THIRDSING + COMP1 + COMP2 + SUPER1 + SUPER2 + ADVR1 + ADVR2 + AGT
            morphs.append(m)
            mPL.append(PL)
            mPOSS.append(POSS)
            mPAST.append(PAST)
            mPROG.append(PROG)
            mPERF.append(PERF)
            mTHIRDSING.append(THIRDSING)
            mCOMP1.append(COMP1)
            mCOMP2.append(COMP2)
            mSUPER1.append(SUPER1)
            mSUPER2.append(SUPER2)
            mADVR1.append(ADVR1)
            mADVR2.append(ADVR2)
            mAGT.append(AGT)

    av = sum(morphs)/len(morphs)
    return(av)
    
#######################
## get mother's MLU ###
#######################
def MOT (file):
    removelist = ['\t', '\r']

    with open(file,'r') as f:
        text = f.read()
        for item in removelist:
            text = text.replace(item, '')
        text = text.split('\n')

        # make a list with only the POS lines from the transcript
        utt = []
        for s, val in enumerate(text):
            if val.startswith('*MOT'):
                m = str(text[s+1])
                m = m[5:]
                utt.append(m)

        morphs = []
        mPL = []
        mPOSS = []
        mPAST = []
        mPROG = []
        mPERF = []
        mTHIRDSING = []
        mCOMP1 = []
        mCOMP2 = []
        mSUPER1 = []
        mSUPER2 = []
        mADVR1 = []
        mADVR2 = []
        mAGT = []

        for s in utt:
            base = s.count('|')
            PL = s.count('-PL')
            POSS = s.count('POSS')
            PAST = s.count('&PAST')
            PROG = s.count('-PROG')
            PERF = s.count('&PERF')
            THIRDSING = s.count('&3S')
            COMP1 = s.count('-CP')
            COMP2 = s.count('&CP')
            SUPER1 = s.count('-SP')
            SUPER2 = s.count('&SP')
            ADVR1 = s.count('-ADVR')
            ADVR2 = s.count('LY')
            AGT = s.count('-AGT')


            m = base + PL + POSS + PAST + PROG + PERF + THIRDSING + COMP1 + COMP2 + SUPER1 + SUPER2 + ADVR1 + ADVR2 + AGT
            morphs.append(m)
            mPL.append(PL)
            mPOSS.append(POSS)
            mPAST.append(PAST)
            mPROG.append(PROG)
            mPERF.append(PERF)
            mTHIRDSING.append(THIRDSING)
            mCOMP1.append(COMP1)
            mCOMP2.append(COMP2)
            mSUPER1.append(SUPER1)
            mSUPER2.append(SUPER2)
            mADVR1.append(ADVR1)
            mADVR2.append(ADVR2)
            mAGT.append(AGT)

    av = sum(morphs)/len(morphs)
    return(av)