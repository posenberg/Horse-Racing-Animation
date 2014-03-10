import time
import os
import random
##CLEAR SCREEN FUNCTION##
def clearScreen():
    if os.name == 'posix': 
        os.system('clear') 
    elif os.name == 'nt': 
        os.system('cls')

TITLESCREEN=['''





                                                      D8                                
                                                     NDD                                
                                                     ONZ                                
                                                    DDN                                 
                                                  8D8DD        D8                       
                                                  DDDDD      ZNDDDDD                    
                                                 8DDDD8    OMD8DDDNDDD                  
                                                 DDD   NNOZNDDDDNDD8DDD8                
                                                O88D     DDDDDDD8 :    O                
                                   ZDDDNDD8    DDDDDDNNDD8DDNNNN                        
                              ZDDDDDDDDDDDDDDDNNNNDDNNDNDDDNNNDZ                        
                         ZDDDDDZ8DD8DDDDDDDDDDDDNDDDDDNMDDDDNDD                         
                    DD  ODDDN   NNDDDDDDNDNDDDDDDDDDDDDDDDDDNN                          
                    78D8DD       DDDDDDDNDDDDDDDDDD8DDND8D8DN                           
                                  DDDDDDDDDDDDDDDDDDDDDDDDDD                            
                             MNNDDDDDDD8  8NDDDDDDDDDDNDNDD8                            
                            NDDDDNDN8       OMNDDDDNNDDNND                              
                             N  ND                   NDDD                               
                             M   7N                 ZMD                                 
                           OD     MD               NO                                   
                           NN       D       MMN     D                                   
                                    N           ONND                                    
                                                   M                                    
                                                   D                                    
                                                    NN                                  



                                                                                        ''','''





                                                      7O7                               
                                                      DDD                               
                                                      8DD                                
                                                     D8D                                 
                                                    DDDD      7NZ                       
                                                   88NDD    NDDDDDNO                   
                                                  DDDNO    ZODDDDDDDN8                  
                                                 DDDODD   DDDDDDDDDDDND                 
                                                 NNDO    DDDDDDDDZZODDND                
                                      8D8        ZNNN88D8D8DDD8D Z                      
                                   8DDNDDDDDDDDDDDDDDDDDDDDDDD8                         
                              O8NNDNDD8DDDDDDDDNDDDDDDDDDDDDNNN                         
                         7NNDND   DDDND88DDDDDDDDND8DDDDDDNDNN                          
                   ON8  NDDDN    ONDDDDDDDDDDDDDDDDDDDDDNDNND                           
                    ODDDDN7       N8DD8DDDDDDDDDDDDDDDDDDDDDN                           
                     8NM            ODDNDNDDDDDDDDDDDDDDDDDDZ                           
                                     DDDDD8   ON8DDDDDNDDDD7                            
                                  ZND87 NN          ZDDDDD8                             
                                  8ND   DO          DDD  8DD                            
                                     8D8D8          DN     ND                           
                                       78  DDD     ODDD  DNND                           
                                       OD     ON 7DN                                    
                                          788NN8                                        






                                                                                     ''','''





                                                       8MMM                             
                                                        MNM                             
                                                      MMM                               
                                                    DMMMM       O                       
                                                   OMMMMN      MMNMM                    
                                                   7MMMM      MMMMMNNN                  
                                                   MMMMMM    MNMMMMNMNMM                
                                                   MMM   MMMMMMMNMMMMNMMMM              
                                        NMN        MMMNOOMMMMMMMN8 O8   M               
                                     8MMMMMMMMMMMMMMMMMMMMMMMMMMM                       
                                   DMMMMMMMMMMMMMMMMMMMMMMMMMMMMM                      
                            NMMMMM78MMMMMMMMMMMMMMMMMMMMMMMMMMMM                        
                          MNM88MMMZDMMMMMMMMMMMMMMMMMMMMMMMMMMM                         
                      MMNNMO        MMMMMMMMMMMMMMMMMMMMMMMMMMM                         
                      ZMM            OMMMMMMMMNMMMMMMMMMMMMMMMD                         
                                        ZMMMMM OMMMMMMMMMMMMMM                          
                                       :MMMMMM    OMMMMMMMNMMMMO                        
                                       MM   MM        7MM      ZMN                      
                                       NNMMMMM8       7MN      OM                       
                                             MMM8M     M   MMMM                         
                                                 OMMN8NM                                







                                                                                         ''','''





                                                        MMM                             
                                                       :NMNN                            
                                                       NMM7                             
                                                     MMMMM                              
                                                    MMMMM                               
                                                   8NNMM8      8NNNNNN                  
                                                  7MMNMMM     MMNNNNDNDM                
                                                  MMMM  ZMOZDMNMNNNDNNDNM               
                                                  OMMM   7MMNNMMNNN ODNNDDN             
                                       MMNMMMM88MNZOMMMMMMMMMMNNNN      8N              
                                    NNMMMNNNNMNMNMMMMMMMMMNNNNNNN                       
                          8MMMMNNNNNNMNMNNNNMNMMNNMNMMMMMNMMNNNN                        
                        OMNNNNNMNM NMMNMNNNNNNMNNMMMMMMMMMMMNNNM                        
                       8MMNM       ZNNNNNNNNNNNNNNNNNNNNMNNNNNND                        
                    MDNNN8          ONNNNNNNNNNNNNNNNMNMMNNNNMM                         
                     MM               NNNNNNNNNNNNNNMNMNNMNNMMDNDD8                     
                                         NMNNN 8MNMNNNNMNMNMNMMNO  ZO                   
                                          MNNM            MMND      O                   
                                           NNNN              7M7    D                   
                                           MNOODMMMM     M7 7NM     N                   
                                           MM8       NM7           88                   
                                             NM                                         
                                              7MN                                       
                                                NN8                                     
                                                  MM                                    



                                                                                         ''','''




                                                        M                               
                                                      MNM                               
                                                      ZMMM                              
                                                     NMM                                
                                                   MMMMN                                
                                                  MMNMMZ        NND                     
                                                 OMMMM7      ZOMMNMND                   
                                                ZMMMMNM    7ZMNMNNNNNN                  
                                                MMMM   OMMMNNNNNNNNMNNMN                
                                                 NMN8 ONMMMMNNNNM7  MMNNMZ              
                                    NMMMMMMMMNMMMMMMMMMNNMNMNNNN                        
                         Z ZZ8OO8NNMNMMMMNMMMMNMMMMMMMMMNNNMMMM                         
                       NDMNNDDMZ  NNMMMMMMMNMMMMMMMMMMMMNNNMMM7                         
                     NNDMMZ      NNMNMMMNMMMMMMMMMMMMMMMMMMMNM                          
                     NNNZ        8MNMMMMMNNMMMNNNMMNMMMMMMNMMN                          
                    DDD           NNMMNNMNNNNNNNNNNNMMMMMNMMMDO                         
                  7N               MMMNNNMNNNNNNMNMNMMNMMNNMMNNMNN7                     
                                    MNNM DNN  O8MMMMMMNMMNDMMMMMNMMD                    
                                    MMM    NM                  N    M8                  
                                   NNM7    NNM                N       MO                
                                  DNM         MMZ          MM          NZ               
                                  OND            NN8                                    
                                   NN               DD7                                 
                                    N7                                                  
                                     N8                                                 




                                                                                        ''','''




                                                       MMM                              
                                                       MMM                              
                                                      ZMNZ                              
                                                    MNMMD                               
                                                  OMMDMM                                
                                                 MNNNMO        78NNNN                  
                                                  NNMNNMZ     NMNNNNMNMD                
                                                 MMMM   8MD ONNNNNNNNNNM8               
                                                 MNMN     NNNNNNNNNNNNNMMN              
                                                  DMMMDMNNNNNNMNMNZ  7MMMMN             
                                   8MMNMMNNMNMNNMMMNNMMMNNNNNNMMM       NMD             
                        DNNNNNNMMMNMNNNMMNNNNNNNNNNNNNNNNNNNNNNM                        
                    NMNMNMMZ     MNNNNNNNNNNNNNNNNNNNNNNNNNNNMM                         
                     MND         MNMNNMMNNMNNNNNNNNNNNNNNNNNNNM                         
                   ZMM7          MMNMMNNMMNNNNNNNMNNNNNNNNNNNNM                         
                   NM            MNMNNNNNNNNMNNNNNNNNNNNNNNNNNNNMMMM8                   
                                 MNNNMNNNN:  8MMNNNNNDNNNNNNNNNDM7  M                   
                                MNMO : MMD                      NMMZ8                   
                             7MNM8     OMM                         MM                   
                             MMN        ND                          NM8                 
                            DM          MM                         M   OMD              
                          7MZ           M8                                M             
                           MO             MZ                                            
                          ZMZ              MO                                           
                            MM              MNMM                                        
                            7N                777                                       

                                                                                        ''','''




                                                        MNN                             
                                                        ONN8                            
                                                         MN                             
                                                      MMNMO                             
                                                    8NNMNN                              
                                                    MMNMN           ZNNN                
                                                   NMMMNMD      ZNNNNNNNN              
                                                   MMMM  Z8M88MMMNNNNNNNNN              
                                                   MMMD   7NMNNNMNNNMNNNNNN8            
                                                    MMMMMNNMNNNNNNNMZ   MNNDD           
                                 NMMMMMNMMMMMMNNNMMMMMMMMNMNMNNNNNM       8M8           
                         78NMMMMM8 MMMMMMMMMMMMMMMMMMMMMMMMMMNNNNZ                      
                      OMMMMMMM    DMMMMMMMMMMMMMMMMMMMMMMMMMMNMMN                       
                   MMMMMD7        MMMMMMMMMMMMMMMMMMMMMMMMMMMNMND                       
                                  MMMMMMMMMMMMMMMMMMMMMMMNMMMMNN                        
                                 NMMMMMMMNMMMMMMMMMMNNMMMNMMMNMNNMN                     
                                MMMMMMM        DMMMMMMMMMMMNNNNNDNNNMMN                 
                             NMMMONMNN                        MMN      8D               
                           MMD  DMMM                           DN         NZ            
                         ZMZ   OMM                               MZ         M           
                       MM      O8                                 MO                    
                   MMNO7     7MO                                  MM                    
                               M                                    M8                   
                             M8                                    NN7                 
                             Z8MM                                    NM                 



                                                                                        ''','''






                                                      DNNO                              
                                                       MD8                              
                                                     DDD                                
                                                    8DDN                                
                                                  88DDDO                                
                                                  DDDDDN       D8DZ7D88                 
                                                  DND  ONM    ZD8888D8DO                
                                                 NDD7      NDD888888888888              
                                                 ZDDZ   8DDDD8D888DDDDD8888             
                                 ZO8D8DDD8        ZDDDDDDDDDD88D8DN    OND8D            
                             ODNZ DDDDDDDDDDD8DDDDNDDDDDDDDDDD8D88        O             
                   DMNMNMNNNDN7  DDDNNDDDDDDDDDDNDDDDDDNDDDDDD8D8                       
                  8NNNNNNNN7    ZNNNNDDDDDDDDDDDDNDDDNDDNDDDDDD8                        
                                8NNDNDDNDDDDDDDDDDNDDNNDDDDDD8DD                        
                                MNNNNNNNNNNDDNDDDNDDDDDDDDD8DD8D                        
                              NNNMDDM      ZNDNDNDDDDNDDDDDDNDDDD8                      
                          NDDNDNNN               ZO88DDNDDDDD   DNDN                    
                      :ZND7  ONM                           DD       D8Z                 
                  NNDNM     NM                             DD           DZ              
                           88                              DD             O7ZD          
                          NO                               DD                           
                        8N                                  D                           
                      DN                                    O                           
                                                            7DZZ                        



                                                                                         ''','''






                                                     NND                                
                                                     ODND                               
                                                      N8                                
                                                   DNDNO                                
                                                  MNNDN                                 
                                                 NNNNND        ZDNDNNN                  
                                                 DNNNNNMZ      NDNNNNNN                 
                                                7NND    ZMO ZNNNNNNNNNNN                
                                                DNNM     DDNDNNNNNMNMNNNNM              
                                   D8DD8Z         NNNDNNNNNNNNMNNNM   MMNNMO            
                            8DNDNDDDDDDDDDDDNNNDNNNDNDNNNNNNNNNNNN:       D            
                  D8ODD8ZODDND  NNDNNDDNDDDNNDNDNNNNDDNNNNNNNNNNM                       
                   8DN8NDDNM    NNNNNNNNDNNNNDDNNNNNNNNNNNNNNNND:                       
                     O88        NDNNDDDNNNNNNDNNNNNNNNNNNNNNNNN                         
                                DNDNDDNNNMDNNNNNNNNNNNNNNNNNNN                          
                          7DDNNDNDNDNNZ   NMNNNNNNNNNNNMNNMMNN                          
                        N8DDDNNNND8        8NMNNNNNMNMNMNNNNM7                        
                        DDDDNO                      ZNND    NMN8                       
                      7DDNMZ                         MNZ       8MD                      
                  ZD8DDD                            NM           DM8                    
                                                   8N              88                   
                                                  OD                 MZ                 
                                                  D                   DNO               
                                                 NZ                     NN              
                                                   NO                                   



                                                                                         ''','''






                                                      MMM                               
                                                      NMMN                              
                                                      NMO                               
                                                    MNMM                                
                                                   8MNNM          ON                    
                                                  7MMMMN       NOMNMMM7                 
                                                  MMMMMMM     DNMNMMMNMM                
                                                  MMNM   MMMMMMMMMNNMMMMMM              
                                                  MMMM   8MMMMMMMMMOZ8MMMMM             
                                  8NMMMMMMMMMD8ZOMMMMMMMMMMMMMMMMM8      87             
                           ONMMMMDMNMMMMMMMMMMMMMMMMMMMMMMMMMMMM8                      
                      MMMNMMMMMM  MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM                       
                       MMNMMM     MMMMMMMMMMMMMMMMMMMMMMMMMMMMMZ                        
                                  ZMMMMMMMMMMMMMMMMMMMMMMMMMMMD                         
                              OZ   MMMMMMMMNMMMMMMMMMMMMMMMMMM7                         
                             DMMMMMMMMMMM    MMMMMMMMNMMMMMNNZ                          
                            NM  MO                ODMMMMMMMM                            
                           7M    M                   ZMMMNM7                            
                        MMMM     ON                  MM7 MM                             
                        Z       7MZ                 MM   NM                             
                                 N                 DM    MM                             
                                           8NMMMNO        M                             
                                                          M                              
                                                          OMD8                          




                                                                                         ''','''

                                                                                        
                                                                                        
                                                                                        
                                                                                        
                                                                                       
                                                      MMM                               
                                                     MMMM                               
                                                     ~MMM                               
                                                    DMMN                               
                                                   MMMMN        DZ                      
                                                  MMMMM      ZMMMMMMN                   
                                                  MMMMM     DMMMMMMMMMO                 
                                                 MMMMDMMM  8MMMMMMMMMMMM                
                                                 MMMM   ZMMMMMMMMNZDMMMMM               
                                    8MMMMMMMDZ7MMMMMMMMMMMMMMMMMM8                      
                       777 Z    78MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMO                       
                    8MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMN                        
                    OMMMMMMMMMM7  MMMMMMMMMMMMMMMMMMMMMMMMMMMMM                         
                      MMMMM       MMMMMMMMMMMMMMMMMMMMMMMMMMMM                          
                                   DMMMMMMMMMMMMMMMMMMMMMMMMM                           
                                Z8MMMMMMMM8DMMMMMMMMMMMMMMMMM                           
                                MMMNNMMMZ      78MMMMMMMMMMO                            
                                 MM DMM              MMMM                               
                                  DMMNMO           8MM MM                               
                                   NN   MMD      MMM   MM                               
                                   MN     MD     MM8MMMNM                               
                                    N     DM   ZM                                 
                                               MM7                             
                                               N7                                       
                                                                             
          
                                                                                                
                                                                                       
                                                                                           
                                                                                         ''','''

                                                                                     
                                                                                        
                                                                                        
                                               MM                                       
                                              MMMM                                       
                                              MNMM                                       
                                              MMZ          MM                          
                                             NMMM          7MNMM8                        
                                            MMMMM        MNNNNNMNND                     
                                            MMMMM       8NMMNNNMNNNM                    
                                            NMMMMMMMM78MMMMNM     YN                    
                                             NMMM     MMMMNNN                           
                                             ZMMMMMDMMNMMMMMNN                           
                               NMMMMMMMMMMMMMMMMMMMMMMMMMNNN7                                    
                          M777MMMNMMMMMMMMMMMMMMMMMMMMMMMNMND                              
                        MM777NMMMMMMMMMMMMMMMMMMMMMMMMMMMMNM                             
                       NNMMM NMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNN                                      
                         NMM NNMMMMMMMMMMMMMMMMMMMMMMMMMMNMMN                             
                          NN  NMMMDZMMMMMM7MMMNMMMMMMMMMMMMMN                             
                          N    NN MMMM     7MNMMMMMMNMMNM                               
                                MMMMM                MMMN                               
                                 NMMD               ZMOMM                              
                                 MMM                OM~MM                             
                                MNM                 NN NM                                
                                M M                 8  7M                  
                               77M 7N               M   M                              
                               DM  MZ              ZM  7M                                          
                               78N DMN              DD  DN                                
                                    
                                                                                        
                                                                                        
                                                                                                 
                                                                                       
                                                                                         ''']
def animateHorse():
    for i in range(10):
        for i in range(len(TITLESCREEN)):
            clearScreen()
            print(TITLESCREEN[i])
            time.sleep(.095)



animateHorse()