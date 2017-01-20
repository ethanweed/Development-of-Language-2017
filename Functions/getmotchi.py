def getmotchi (file):
    with open(file,'r') as f:
        text = f.read()

        lines = text.split('\n')
        clean_list = lines
        clean_list = [s.replace('\t', '') for s in clean_list]
        clean_list = [s.replace('\r', '') for s in clean_list]
        #clean_list = [s.replace('*FAT', '*MOT') for s in clean_list] #NB FAT 2 MOT!
        #clean_list = [s.replace('*AUN', '*MOT') for s in clean_list] #NB AUN 2 MOT!
        clean_list = [s.replace('!', '') for s in clean_list]
        clean_list = [s.replace('?', '') for s in clean_list]
        
        # make a list with only the MOT and CHI lines from the transcript
        utt_motchi = []
        utt_chi = []
        utt_mot = []
        for s, val in enumerate(clean_list):
            if val.startswith('*MOT'):
                utt_motchi.append(str(clean_list[s]))
                utt_mot.append(str(clean_list[s]))
            if val.startswith('*CHI'):
                utt_motchi.append(str(clean_list[s]))
                utt_chi.append(str(clean_list[s]))
        
        return(utt_motchi)
    
def getchi (file):
    with open(file,'r') as f:
        text = f.read()

        lines = text.split('\n')
        clean_list = lines
        clean_list = [s.replace('\t', '') for s in clean_list]
        clean_list = [s.replace('\r', '') for s in clean_list]
        #clean_list = [s.replace('*FAT', '*MOT') for s in clean_list] #NB FAT 2 MOT!
        #clean_list = [s.replace('*AUN', '*MOT') for s in clean_list] #NB AUN 2 MOT!
        clean_list = [s.replace('!', '') for s in clean_list]
        clean_list = [s.replace('?', '') for s in clean_list]
        
        # make a list with only the MOT and CHI lines from the transcript
        utt_motchi = []
        utt_chi = []
        utt_mot = []
        for s, val in enumerate(clean_list):
            if val.startswith('*MOT'):
                utt_motchi.append(str(clean_list[s]))
                utt_mot.append(str(clean_list[s]))
            if val.startswith('*CHI'):
                utt_motchi.append(str(clean_list[s]))
                utt_chi.append(str(clean_list[s]))
        
        return(utt_chi)
    
def getmot (file):
    with open(file,'r') as f:
        text = f.read()

        lines = text.split('\n')
        clean_list = lines
        clean_list = [s.replace('\t', '') for s in clean_list]
        clean_list = [s.replace('\r', '') for s in clean_list]
        #clean_list = [s.replace('*FAT', '*MOT') for s in clean_list] #NB FAT 2 MOT!
        #clean_list = [s.replace('*AUN', '*MOT') for s in clean_list] #NB AUN 2 MOT!
        clean_list = [s.replace('!', '') for s in clean_list]
        clean_list = [s.replace('?', '') for s in clean_list]
        
        # make a list with only the MOT and CHI lines from the transcript
        utt_motchi = []
        utt_chi = []
        utt_mot = []
        for s, val in enumerate(clean_list):
            if val.startswith('*MOT'):
                utt_motchi.append(str(clean_list[s]))
                utt_mot.append(str(clean_list[s]))
            if val.startswith('*CHI'):
                utt_motchi.append(str(clean_list[s]))
                utt_chi.append(str(clean_list[s]))
        
        return(utt_mot)