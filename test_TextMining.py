
# coding: utf-8

# In[2]:


#import pyodbc
import pandas as pd
import re
df = pd.read_csv("C:\\Users\\vzhang1\Documents\\tables\Close_Description.csv",header=0) 
df.head(10)


# In[6]:


pd.set_option('display.max_columns', None)  

textdata = list(df['Description'])
print(textdata[7]) ##Description as an email
len(textdata)


# In[73]:


#RE For Data Cleaning
textdata= [[re.sub(r'(\n)+|(\xa0)+|(\r)+', ' ',item.lower())] for item in textdata]
textdata= [[re.sub(r'[^\w\s]', ' ',item[0])] for item in textdata]
textdata= [[re.sub(r' +', ' ',item[0])] for item in textdata]


# In[74]:


'''
for i in range(4):
    print (textdata[i])'''


# In[75]:


#colelction of all words
collection_words = [" ".join(textdata[i]).split(" ") for i in range(len(textdata))]
#print(collection_words)
res = []
_ = 0
while _ < len(textdata):
    res += collection_words[_]
    _ += 1

res
    


# In[76]:


import matplotlib.pyplot as plt
import collections as CT

plt.hist(res, bins='auto')
plt.title("Histogram with 'auto' bins")
plt.show()
count = CT.Counter(res)
#print (sorted(set([i for i in res if res.count(i)>5])))


# In[77]:


sorted(count, key = lambda x: count[x])[::-1]


# In[78]:


#try nltk for word token
import nltk
#nltk.download('punkt')
#nltk.download('averaged_perceptron_tagger')
#nltk.download('maxent_ne_chunker')
#nltk.download('words')
from nltk import word_tokenize, pos_tag, ne_chunk
sentence = 'Exam completed the commitment showing lots 15 16 but only one parcel for lot 16 title clearance initially spoke with the consumer on 2 1 the consumer stated that they had a deed prepared recorded that intended to grant lot 15 to his daughter laura preston this deed included the correct legal description in the body of the deed but the attached exhibit for both lots 15 16 the consumer verified that title source could prepare a deed to correct this situation and transfer lot 16 back to the consumer tc ordered a deed that incorrectly included the entire legal for lots 15 16 should have included lot 16 only and emailed the deed to laura preston to execute the legal description was hand corrected by laura and taken directly to the county to be recorded instead of being returned to title source for review 17 for deed recording was not removed from the cd the closing was pushed back twice on the day of closing first for delay in receiving closing docs from chase and the second for trouble securing a notary the consumer called from closing indicating that the legal description in the closing package was still incorrect listing both lots the file was placed in delay for hand corrections to the legal description and missing qcd notes from tc were not clear that the consumer had the deed recorded on their own and it had already been added to title the legal was corrected after closing and attached to the dot and sent to the county for recording sent coaching to exam title clearance and typing leadership '
print (ne_chunk(pos_tag(word_tokenize(sentence))))


# In[1]:


#allwords
strall = ''
for _ in textdata:
    strall += _[0]
#strall


# In[80]:


'''from collections import Counter
strall = ' '
for _ in range(len(textdata)):
    strall.join(textdata(_))
unique_words = list(set(" ".join(textdata).split(" ")))
def make_matrix(text, vocab):
    matrix = []
    for item in headlines:
        # Count each word in the headline, and make a dictionary.
        counter = Counter(headline.split())
        # Turn the dictionary into a matrix row using the vocab.
        row = [counter.get(w,0) for w in vocab]
        matrix.append(row)
    df = pd.DataFrame(matrix)
    df.columns = unique_words
    return df

print(make_matrix(headlines, unique_words))'''


# In[81]:


#building of dictionary
word_teams = ["Mortgage Ops",
"Capital Markets",
"Default Ops",
"Payment Services",
"Training",
"Appraisal",
"Client Relations",
"Commercial",
"Deed Team",
"Escrow",
"Final Policy",
"Recording Recon",
"Recording Resource",
"Recording Send Out",
"Title Clearance",
"Title Production",
"Underwriting",
"Team Caption ",
"Direct Mail",
"Cust Service",
"Escrow",
"FSBO",
"Communications",
"ARM and HELOC",
"Capital Markets",
"Cash Team",
"Client Relations",
"Default Ops Vendor",
"Foreclosure",
"Invoice Management",
"Legal",
"MapIT",
"Mortgage Insurance",
"Ops",
"ORM Ops",
"Servicing",
"Tax Payment",
"Tax Research",
"Technology",
"Appraisal",
"Cali",
"Client Relations",
"Commercial",
"Deed Team",
"Escrow",
"Escrow Accounting",
"Final Policy",
"Notary Vendor Management",
"Original Documents",
"Recording Final Docs",
"Recording Resource",
"Recording Send Out",
"Sales",
"Title Clearance",
"Title Comm. Spec.",
"Title Production",
"Team Member Referral Coor",
"Team Relations Specialist",
"Title Clearance Vesting",
"AccounPayable",
"Associate Counsel",
"Business Consulting",
"Client Relations",
"Communications",
"Marketing Strategist",
"Ops",
"ORM Training",
"Partner Manager - Specialty",
"Pricing Regulator",
"Property Pres & REO",
"Purchase-Title",
"QLMS-CCS",
"Servicing Advance Governance",
"Technology",
"Appraisal",
"Appraisal Partner Management",
"Audit and Compliance",
"Client Assurance",
"Client Experience",
"Escrow",
"Hotline",
"Rec. Re-Record",
"Recording Recon",
"Reg Staff Appr",
"Technology",
"Title Partner Management",
"Title Production",
"Training",
"Clearance Auditor",
'Reimbursement',
'exam',
'closing'
'tc']
word_teams = list(set(word_teams))
print ('word_teams:', word_teams)










word_teammember_title = ["Software Engineer",
"Senior Business Analyst",
"Account Resolution Associate",
"Support  team",
"Accts Payable Specialist",
"Senior Client Care Specialist",
"Associate Escrow Specialist",
"Senior Vendor Analyst - HOI",
"Post Funds Client Services Specialist",
"Origination Resolution Specialist",
"Marketing Program Lead",
"Communication Quality Review Coach",
"Licensing Specialist",
"Quality Ctrl Spec-TS-Exec.",
"Recruiter",
"ISM Assurance Specialist",
"Loss Analysis Specialist ",
"Marketing Strategist",
"Mgr, Technology Support",
"TC, Mortgage Ops",
"Business Analyst Architect",
"Processing Manager",
"Closing Preparation Specialist",
"Associate Banker ORM",
"Junior Designer",
"Client Relations Senior Research Analyst",
"Quality Assurance Analyst",
"Auditor",
"Tm Ldr & Asso Corp Counsl",
"Training Specialist-Ops",
"Closing Support Spec.",
"Accounts Payable Analyst",
"Solution Consultant",
"Cl. Rel. Init. Res. Aud.",
"Partner Relationship Specialist Senior",
"Financial Analyst",
"Executive Purchase Banker",
"Appraisal Rel. Spec-Exec",
"Default Ops Closing Senior",
"App. Support Analyst",
"Tax Research Senior",
"Ambassador",
"Pricing Analyst",
"Resolution Specialist",
"Executive Solution Underwriter, QLMS",
"Power Banker",
"President's Club Underwriter",
"Relatinshp Mgr, Relo Svcs",
"Senior Operations Trainer",
"Purchase Banker",
"Escrow-Post Close Client Services",
"Inv. Reporting Analyst",
"REALTOR",
"Mortgage Termination Specialist",
"Program Manager",
"Desktop Tech",
"Content Strategist",
"Product Manager",
"Client Advocate - Scribe",
"Taxes Analyst",
"Executive Vice President",
"General User",
"Underwriter",
"Original Document Specialist",
"Client Communicator",
"Bus Intelligence Devloper",
"DTRT Analyst",
"Commercial Post Closing Specialist",
"Mortgage Banker",
"Cash Balancing Auditor",
"Refi Escrow Closer-Exec",
"Executive Client Care Specialist",
"Commercial Tax Analyst",
"Senior Copywriter",
"Appraiser Communication Specialist-Exec",
"Closing Lifesaver",
"Quality Assurance Manager",
"Final Doc Spec, ORM",
"Gov't Insuring Resolution Analyst",
"Quality Control Auditor",
"Servicing Senior Trainer",
"Salesforce Administrator",
"Purchase Delay Specialist",
"Campus Ambassador",
"Branch Manager",
"Insurance Loss Senior",
"Associate Collateral Underwriter",
"Email Envoy",
"Examiner",
"Taxes Clerk",
"Discharge Spec Final Docs",
"Internal Auditor",
"Security Officer",
"Client Relations Resolution Specialist",
"Capital Market Analyst",
"Test",
"Client Advocate",
"Spec. Loans Client Communication Analyst",
"Administrator",
"Chairman",
"Senior Purchase Solution Consultant",
"Invoice Management Associate",
"Marketer",
"Purchase Processor",
"Licensing Analyst",
"SQA Engineer",
"Amaze U Coach",
"QLMS President's Club CARE Specialist",
"Underwriter ORM",
"Executive Power Banker",
"Executive QLMS Closing Specialist",
"Associate Banker (Quicken Loans)",
"Client Relations Spec.",
"Admin Support",
"Commercial Typist",
"Continuous Imprv Analyst",
"Executive Closing Specialist",
"Client Relations Advocate",
"Security Spec.",
"TC, Capital Markets",
"Bankruptcy Specialist",
"Facilities Support Technician",
"Associate Corporate Counsel",
"Team Relations Specialist",
"Mortgage Insurance Specialist",
"Special Loans Underwriter",
"Training - Consultant",
"President's Club Closing Specialist",
"Escrow Accounting Analyst",
"Purchase Closing Spec.",
"Client Solut Intake Assoc",
"Marketing Specialist",
"Modeler",
"Operations Analyst",
"Commercial Support Specialist",
"Senior Resolution Analyst",
"Senior Software Engineer",
"PC Closing Care Spec.",
"Senior Purchase Specialist",
"Background Specialist",
"Senior Modeler",
"Appraisal Status Coordina",
"TC, TS Exam",
"Exec. Closing Care Spec.",
"Executive Vendor Analyst-Condos",
"Loan Opener",
"Final Policies Specialist",
"Purchase Closing Specialist",
"Lead Cl Rel Research Spec",
"Solution Architect",
"Build & Release Engineer",
"FSO Underwriter",
"QLMS Closing Specialist",
"Junior Escrow Officer",
"Executive Vendor Analyst – VFSO",
"Facilities Technician",
"Assoc. Collateral UW",
"Accounts Receivable Anlst",
"Executive ISM Assurance Specialist",
"Vendor Compliance Officer",
"Senior Vendor Analyst-Condos",
"Partner Analyst",
"SQA Architect",
"DBA",
"Client Care Specialist",
"Associate Purchase Processor",
"Client Service Specialist",
"Bus. Metrics Analyst-Client Experience",
"Loan Analyst",
"Client Experience Analyst",
"Escrow Lifesaver Senior",
"Insurance Loss Specialist",
"PC Purchase Solut Consult",
"Escrow Administrator",
"Capital Markets Analyst",
"iFile Clerk",
"Purchase Escrow Specialist",
"Account Advisor",
"Client Feedback Analyst",
"Commercial Project Manager",
"Appraisal Data Analyst",
"Graphic Designer",
"Vendor Analyst - Subs",
"Business Continuity Analyst",
"BI Business Analyst Architect",
"Client Solutions Vendor Associate",
"TC, Communications",
"Partner Compliance Officer",
"Purchase Liaison",
"Software Ent. Architect",
"Original Document Spec.",
"Foreclosure Associate",
"Training Consultant",
"Banker Licensing Support Specialist",
"Transaction Manager",
"Bizdom U",
"Banker Lic. Underwriter",
"SOS Servicing Specialist",
"Document Resolution Analyst",
"Office Specialist",
"Senior Closing Care Rep",
"Appraisal Billing Specialist",
"Outbound Call Center Rep.",
"Relationship Manager",
"Commitments Clerk",
"Tech Support Analyst",
"Senior Client Advocate",
"Advanced Analytics Business Analyst",
"Senior Closing Underwriter",
"Servicing Resolution Specialist",
"Brainforce Specialist",
"Intern",
"Chase Closing Processor-Exec",
"Underwriting Training Sp.",
"HR Administrator",
"Receptionist",
"Business Sys Analyst",
"Executive Resolution Advocate",
"Mailroom Courier",
"Assignment Analyst",
"President",
"Resolution Advocate",
"BI Engineer",
"Creative Coordinator",
"Closing Coordinator",
"SLK Typist",
"Accounts Payable Clerk",
"Mgr, Special Projects",
"Resolution Correspondent",
"Client Experience Spec.",
"Folder Receive Analyst",
"TS Associate Appraisal Analyst-Exec",
"CEMA Processor-Exec",
"Resolution Anlst Final Doc",
"Preclose Specialist",
"Recording Auditor",
"OTHER",
"Senior Legal Analyst",
"Closing Prep Specialist-S",
"Trainer",
"Appraisal Review Analyst",
"Detection Analyst",
"Data Scientist",
"Mail & Print Support Specialist",
"Balancing Auditor",
"Processing Supervisor",
"iClosing Processor",
"Business Metrics Analyst",
"Client Package Coordinator",
"App. For Success Spec.",
"TS Talent Strategist",
"Appraisal Reconciliation Analyst",
"Lead Client Advocate",
"Agent Coordinator",
"Client Solut Closer Assoc",
"PC Social Media Advocate ",
"TS Exceptions Analyst",
"Accounting & Financial Reporting Manager",
"Onsite Representative",
"Loan Boarding Project Mgr",
"Regional Assistant",
"Cashiering Auditor",
"Appraiser Comm Specialist",
"Investor Reporting Analyst",
"TC, TS Client Experience",
"Senior Partner Resolution Specialist",
"PC Hunt Purchase Specialist",
"President's Club Power Banker",
"Performance Engineer",
"Underwriting Training Specialist",
"Appraiser Complaint Spec.",
"Systems Engineer",
"Account Executive",
"Admin Assistant",
"TC, TS Escrow",
"Servicing Coach",
"Senior Accounts Payable Analyst",
"Staff Appraiser Support Specialist",
"Enterprise Architect",
"Recording Clerk",
"Vendor Analyst - VOE",
"Collateral UW - QL",
"Senior Mortgage Termination Specialist",
"Senior Social Media Advocate",
"Executive Vendor Analyst-Vending Machine",
"PC Power Banker",
"Project Engineer",
"Senior Power Banker",
"Project Coordinator",
"PC Refi Escalation Specialist",
"Associate Software Engineer",
"Partner Resolution Specialist",
"Associate Underwriter",
"CORP",
"Technical Support",
"Training Specialist",
"Commissions Analyst",
"Associate Banker",
"Data Warehouse Engineer- Big Data",
"Senior Systems Architect",
"Deputy General Counsel",
"Quality Control Analyst",
"LENDER",
"ATTORNEY",
"SQA Analyst",
"Amazement Coordinator",
"Recording Analyst",
"Escrow Analysis Guru",
"Spec. Mortgage Advocate",
"Senior Research Specialist",
"Project Manager",
"Exec Business Analyst",
"PC Resolution Advocate",
"Special Loans Loan Boarding Specialist",
"Disbursement Analyst",
"Executive Vendor Analyst",
"Account Specialist",
"Database Administrator",
"Tax Resource Specialist-Executive",
"TS Associate Appraisal Analyst",
"Vice President, Ops",
"Document Spec.- Scanner",
"Vendor Analyst",
"Tax Resource Specialist-Senior",
"Default Ops Closing Specialist",
"Partner Management Specialist",
"Appraisal Coordinator",
"AMC Collateral Underwriter",
"Shipping Coord Final Docs",
"Refi Escrow Closer",
"LC Appraisal Coordinator",
"Resolut. Anlst Final Doc",
"Client Relations Specialist-Senior",
"Claims Specialist",
"HUD Insurer",
"Post Close Specialist ",
"Executive Recruiter",
"LC Appraisal Analyst",
"Exec. Client Care Spec.",
"Copywriter",
"Team Member Referral Coor",
"Escrow Specialist",
"Closing Document Specialist",
"Exec. Solution Consultant",
"IT Security Engineer",
"Recording Analyst-Re-Record-Exec",
"Operations Trainer",
"Project Administrator",
"Jr. Investor Reporting Analyst",
"TC, Client Advocate",
"Tax Analyst-Senior",
"Desktop Engineer",
"Credit Analyst",
"Client Package Coord.",
"BI Developer",
"Chief Valuation Officer",
"Mail Analyst",
"Client Ambassador, QLMS",
"Collateral Coordinator",
"Assoc. Tech Support Spec",
"Chief Info. Officer - TSI",
"Account Executive (NC)",
"Client Ambassador, TS",
"Closing Processor-Exec",
"Data Analyst",
"CEMA Specialist",
"Inventory Control Coord.",
"Client Solut Vendor Assoc",
"Client Resolution Specialist-Senior",
"Foreclosure Specialist",
"Senior Project Manager",
"Document Analyst",
"In-Bound Call Center Rep",
"Client Relations Project Coordinator",
"Client Ambassador",
"Default Ops Closing Associate",
"Communications Coordinator",
"Delay Analyst",
"Exec. Vendor Analyst - Vending Machine",
"Amazer",
"TS Review Appraiser",
"Software QA Engineer",
"Special Loans Analyst",
"Mobile App Developer",
"Executive Social Media Advocate",
"TC, Rec. Follow-up",
"Special Loans Communications TC",
"",
"Deep Dive Analyst",
"CEMA Pre-Close",
"Payment Processor",
"Recording Analyst-Resource-Exec",
"Vendor Relations Analyst",
"President's Club Client Care Specialist",
"Assoc. Closing Coord.",
"MyQL Closing Specialist",
"Paralegal",
"Cash Manager",
"Client Relations Specialist",
"Prpty Preserv/Convey Spec",
"REO Specialist",
"Natural Disaster SPOC",
"Account Manager",
"Tax Payment Specialist",
"Special Loans Lien Analyst ",
"Senior Financial Analyst",
"Talent Specialist",
"Event Coordinator",
"Disbursement Auditor",
"Partner Service Manager",
"SOS Underwriter",
"Delay Analyst-Exec",
"TS Portfolio Manager",
"Executive Vendor Analyst - VFSO",
"Senior Loan Analyst",
"Training Strategist",
"TS Communications Special",
"Property Analyst",
"Corporate Advance Assoc.",
"Junior Underwriter",
"Client Resolution Spec.",
"PC Purchase Solution Consultant",
"President's Club Loan Analyst",
"Courier",
"Junior Video Editor",
"Appraisal Assigning Coor",
"Chase Closing Processor",
"Executive Client Advocate",
"Partner Support Analyst",
"President's Club Purchase Specialist",
"Cl Rel Exec Research Spec",
"Acquisition Specialist",
"Senior Underwriter QL",
"Senior Corporate Counsel",
"Quality Review Analyst",
"Govnmt Insuring Speclst",
"Resolution Analyst",
"Rocket Launcher",
"Warehouse Auditor",
"Contractor",
"Temporary Team Member",
"Loss Mitigation Coord",
"Account Exec., TS Sales",
"Senior Client Ambassador",
"Purchase Agreement Underwriter",
"Client Advocate Coach",
"Operations Specialist",
"Executive Purchase Specialist",
"Assoc. Res. Advocate",
"Senior Servicing Resolution Specialist",
"Manager",
"Co-Op Specialist",
"Senior Investigator",
"Business Support Analyst",
"TS Communications Spec.",
"TSI Clearance Auditor",
"Assoc. Client Ambassador",
"Mobile Application Developer",
"IT Security Analyst",
"Executive Assistant",
"Appraisal Status Coordinator",
"Marketing Strategy Spec.",
"Platinum Club Resolution Correspondent",
"Income Specialist",
"Shipper",
"Closing Support Specialist",
"President's Club Solution Consultant",
"Global Business Strategist",
"Agent Relationship Manager",
"Abstractor",
"BUILDER",
"Executive Loan Analyst",
"Loan Processor",
"Software Architect",
"Mousetrapper",
"Pipeline Liaison",
"Administrative Assistant",
"Mrtg Resolution Analyst",
"Launch Pad Specialist",
"Vendor Analyst - Payoffs",
"Client Relations Coach",
"Exec. Hunt Purchase Specialist",
"Customer Service Rep",
"Hazard Insurance Specialist",
"Associate BI Engineer",
"Property Preservation/Conveyance Spec.",
"TSI, E-Commerce Architect",
"Temporary Employee",
"Underwriter QL",
"Training Coordinator",
"PC Purchase Escalation Specialist",
"TS Audit Specialist",
"TC, Accounts Payable",
"Escalation Underwriter",
"Appraisal Project Spec.",
"Appraisal Partner Manager",
"Senior Vendor Analyst",
"Appraisal Billing Special",
"Invoice Management Specialist",
"Servicing Consultant",
"Assoc. Business Analyst",
"Exception Underwriter",
"Auditor, TS",
"Executive Resolution Correspondent",
"Exec. Pur. Solut Consult",
"Purchase Agreement UW",
"Survey Analyst",
"iExaminer",
"Compensation Analyst",
"IT Process Management Analyst",
"Closing Care Specialist",
"Associate Recruiter",
"Tour of Duty Associate",
"Project Manager/Producer",
"Credit Risk Analyst",
"Staff Appraiser",
"Product Support",
"Client Solutions Spec.",
"Appraisal Analyst",
"Accountant",
"Purchase Escrow Spec-Exec",
"Assoc. Client Care Spec.",
"Senior Auditor",
"Tax Analyst",
"Senior Account Executive",
"Software Solution Architect",
"N/A",
"Launch Pad Associate",
"Processor",
"Marketing Strategy Specialist",
"Client Rel Project Coord",
"Exec. Asst, Bedrock",
"Product Analyst",
"Rocket Mortgage Power Banker",
"Appraisal Project Specialist",
"Investor Communications Specialist",
"Executive Underwriter QL",
"Closing Care Rep.",
"Compliance Specialist",
"TC, TS Appr. Vendor Mgmt",
"Hazard Insurance Senior",
"Operations Divisional Vice President",
"Document Processing Spec.",
"Partner Service Specialist",
"Financial Manager",
"Vendor Analyst - Feds",
"TC Post Close Specialist",
"Legal Project Specialist",
"Accounting Spec.",
"National Commercial Account Closer",
"Closing Processor",
"Closing Care Representative",
"Account Exec., TS",
"Business Intelligence Trainer",
"PC Escalation Specialist",
"Purchase Processor-Exec",
"Quality Assurance Specialist",
"Executive Assistant I",
"Application Support Analyst",
"Senior Document Specialist",
"Audio/Visual Specialist",
"Insurance Loss Advocate",
"Typist",
"Post Closing Analyst",
"Account Advisor Associate",
"Co-op Student",
"Vendor Analyst - Condos",
"Vendor Management Specialist",
"President's Club Relocation Purch. Spec.",
"Idea Consultant",
"Desktop Technician",
"Senior Mortgage Banker",
"Jr Closing Processor",
"Appraisal Zone Analyst",
"Project Specialist",
"Associate Continuous Improvement Analyst",
"TC, Ambassador",
"Business Solution Architect",
"Senior Special Loans Underwriter",
"Senior Analyst",
"Accounting Clerk",
"Senior Recruiter",
"Vice President, Investor Relations",
"Tax Specialist",
"Escrow Officer",
"Marketing Coordinator",
"Accounting Specialist",
"Escrow Coordinator",
"Senior Data Analyst",
"Lead Resolution Advocate",
"Innovation Consultant",
"TC, Social Media Advocate",
"Vendor Service Specialist",
"Collateral Underwriter - QL",
"Vendor Service Rep",
"Senior HUD Reviewer",
"TC, TS Onsite Sales",
"Final Doc Specialist",
"Senior BI Engineer",
"BROKER",
"Associate IT Security Analyst",
"Associate Banker - AZ",
"Document Developer",
"Tax Escalation Senior",
"Partner Relationship Specialist ",
"Client Relations Research Analyst",
"Internal Audit Manager",
"Associate SQA Engineer",
"Instructional Designer",
"Social Media Envoy",
"TS Review Appraiser-Exec",
"HUD Reviewer",
"Closing Underwriter QL KY",
"Partner Relationship Spec. Executive",
"Business Development Associate",
"Commitments Typist",
"Deed Specialist",
"Suspense Analyst",
"Closing Document Special.",
"Aerotek Administrative Assistant",
"Senior Foreclosure Specialist",
"Customer Service",
"TS Production Specialist",
"Associate Examiner",
"Senior Amaze U Trainer",
"Client Solutions Closer Associate",
"Application Administrator",
"Team Caption ",
"ORM Trainer",
"Appraiser Communication Specialist",
"Appraisal Recon Analyst",
"TS Quality Review Spec",
"Assistant Commercial Account Closer",
"Foreclosure Rev. Analyst",
"Database Engineer",
"Banker Licensing Supp Sp",
"Quality Assurance Analyst, Servicing",
"Purchase Escrow Spec.",
"Ism Ninja II",
"Escrow Coordinator, Exemp",
"Escrow Services Project Specialist",
"Communication Liaison",
"Final Policy Specialist",
"Senior Vendor Analyst – Condos",
"PC Solution Consultant",
"Closing Underwriter",
"Senior Vendor Analyst - Feds",
"Exec Training Consultant",
"Impact Trainer",
"Specialized Mortgage Advocate",
"Associate Closing Coordinator",
"Escrow Post Close FOC Services",
"Senior Closer",
"Closer",
"Closing Care Rep",
"Executive Amaze U Trainer",
"Web Designer",
"Technical Supp Specialist",
"Assoc System Engineer",
"Software Developer",
"Instruct. Designer, TS",
"D-Ops Liquidation Closing Specialist",
"Quality Control Analyst, Origination",
"Client Rel. Research Spec",
"Business Area Trainer",
"Communications Specialist",
"Document Specialist",
"Commercial Disbursement Analyst",
"Pipeline Analysis Liaison",
"Vice President, Security",
"Operations Coach",
"Senior Copywriter, TS",
"Accounts Receivable Analyst",
"External Staff Appraiser Trainee",
"Business Analyst",
"Assoc Appraisal Analyst",
"Closing Preparation Specl",
"Tax Resource Specialist",
"Exec. Client Care Specialist",
"Recording Analyst - Follow-up Senior",
"PC Client Care Specialist",
"Associate Banker (One Reverse)",
"Senior Refi Escalation Specialist",
"General Counsel",
"Senior Closing Care Specialist",
"Executive Partner Appraisal Specialist",
"Product Analyst, GURU",
"Executive Closing Underwriter",
"Appraisal Relations Spec.",
"Signing Agent Coordinator",
"Tax Payment Senior",
"Senior Database Administrator",
"Closing Document Spec.",
"GRC Specialist",
"Senior Training Specialist-Ops",
"Final Doc Spec.",
"Lead Servicing Resolution Specialist",
"Data Warehouse Engineer",
"Payment Advisor",
"Cl. Rel. Research Analyst",
"Servicing Trainer",
"Default Ops Underwriter Associate",
"Social Media Advocate",
"Tax Research Specialist",
"Client Solutions QA Assoc",
"Relocation Specialist",
"Amaze U Auditor",
"Partner Appraisal Specialist",
"PC Purchase Specialist",
"Exec. Agent Coordinator",
"PC Hunt Client Care Specialist",
"Exec. Purchase Specialist",
"Strategic Analyst",
"PC - QLMS Closing Specialist",
"Senior Business Consultant",
"Sales Manager",
"Senior Closing Care Spec.",
"Exec Partner Coaching Spec",
"Chief Executive Officer",
"Tax Escalation Specialist",
"Executive Instructional Designer",
"Exec. Hunt Client Care Specialist",
"Soft Qual. Assurance Eng.",
"CEMA Processor",
"Lead Client Ambassador",
"Associate Business Analyst",
"CLIENT",
"Associate Closing Specialist",
"Application Support",
"Senior Vendor Analyst - Subs",
"Launch Pad Senior",
"Suspense Underwriter",
"Desktop Technical Support Specialist",
"Senior Compliance Specialist",
"Partner Relations Manager",
"E-mail Coordinator",
"Amaze U Trainer",
"Closing Compliance Specialist",
"Business Consultant",
"Mousetrap Architect",
"TC, TS Escrow Accounting",
"QLMS Closing Coordinator",
"Purchase Support Analyst",
"Appraisal Assigning Coordinator",
"Investigator",
"Client Solutions Underwriting Associate",
"Servicing Quality Analyst",
"External Staff Appraiser",
"Assoc. Closing Specialist",
"Facilities Tech",
"Pipe. Analysis Liaison-Exec",
"Associate Client Care Specialist",
"Communication Specialist",
"Partner Coaching Specialist",
"Loan Review Specialist",
"Communication Quality Review Specialist",
"Loan Officer",
"Marketing Project Manager",
"Analyst",
"Client Resolution Specialist",
"HELOC Specialist",
"Asst. Comm. Acct. Closer",
"Insurance Specialist",
"Post Closer",
"PC Client Advocate",
"Client Experience Specialist",]



word_documents = ["Abstract",
"Ally-QL list ",
"Appraisal Dodd Frank Certification",
"Appraisal Engagement Letter",
"Appraisal Invoice",
"Appraisal Report",
"Closing Instruction",
"Closing Package",
"Collateral Package",
"Cost compare template ",
"Death Certificate",
"Final Docs",
"Final Payoff",
"Form 1003 (Ditech/ Homeward)",
"HOI",
"Legal Description",
"Mortgage",
"Mortgage/Deed of trust - Recorded ",
"Mortgage/Deed of trust - Signed ",
"Notary Package",
"Payoff",
"Policy Package",
"Power of Attorney",
"Purchase Agreement",
"Quote",
"Sub Agreement",
"Subordination Agreement - signed ",
"Subordination Package",
"TC Notes",
"Title Commitment",
                  'Commitment',
"UCDP Submission Summary Report",
"Warranty/Quit Claim Deed",]
print ('word_Documents:', word_documents)



word_ProductCode = ['Title','Appraisal','Closing','Recording','TAX','AVM','SURVEY']

print ('word_ProductCode:', word_ProductCode)


# In[84]:


def findkeyword(string, words):
    return ([word for word in words if string.find(word) > -1]) #BOYER MOORE o(n+m+|Σ|)
i = 7
print(textdata[i][0])
print(findkeyword(textdata[i][0], [word.lower() for word in word_ProductCode]))
print(findkeyword(textdata[i][0], [word.lower() for word in word_documents]))
print(findkeyword(textdata[i][0], [word.lower() for word in word_teams]))


# In[15]:


#import nltk
#nltk.download('wordnet')

#find synonym
from nltk.corpus import wordnet as wn

print("Category name:", wn.synsets('angry'))

print("Synonyms:", wn.synset('angry.s.02').lemma_names())


# In[ ]:


ll = [1,2,3,3,3,2]
ll


# In[63]:


l = ['you are a good person','person']
m = list(map(lambda x: x.split(), l))
print (list(m))
print (list(set([5,5,3,4,6])))
def findkeyword(string, objs):
    return ([obj for obj in objs if string.find(obj) > -1])
findkeyword('you are a sb', ['sb','you','he'])
target = 'No sucker is a good sucker'
target.replace('sucker','')
#['fucker'] += 'sucker'


# In[7]:


def findkeyword(string, objs):
    return ([obj for obj in objs if string.find(obj) > -1]) #BOYER MOORE o(n+m+|Σ|)

#we will want to grab objs with most words first
from collections import defaultdict
def SearchOrder(List_Of_Obj, target):
    list_of_length = list(map(lambda x: len(x),list(map(lambda x: x.split(), List_Of_Obj))))
    dic = defaultdict(list)
    for index, item in enumerate(list_of_length):
        dic[item].append(List_Of_Obj[index])
    #t_of_length, dic)
    
    list_of_length_1 = list(set(list_of_length))
    res = []
    while len(list_of_length_1):
        length = list_of_length_1.pop()
        obj_to_search = dic[length]
        print (obj_to_search)
        searched = findkeyword(target.lower(), [obj.lower() for obj in obj_to_search])
        if searched:
            res.append(searched)
        print (searched)
        for _ in searched:
            target = target.replace(_ , '')
    return [item[0] for item in res]
        
        
    
SearchOrder(['you are a good person','He is a just bad','person','sb is always sb','you','good person','are','good'],
            'You are not a good person')


# In[94]:


#breaking by punctuations(,.?!)
import re
sample = 'The consumer was very confused and was unwilling to provide his full divorce decree. On 5/20 he was advised multiple times that the entire document was required. It appears as though the consumer was upset with Machelle Parker, as she was unable to clearly communicate to the consumer the reason for the requirement. Leadership has confirmed that coaching has been provided to Machelle.  The consumer is transferred to the Team Captain, Brittney Vaughn who provides the same information; still frustrated Andrew requests that the Team leader contact him. Brittney reaches out to Team Leader, Chris Layton via phone advising him of the issue and requests that he e-mail the consumer. Brittney provides detailed notes in ATLAS noting it for leadership review; Brittney states in her note that she advised the consumer   leadership would reach out via an email. This is a Valid NRCC, no recording of outgoing communication to Andrew was located.'
def sentence_break(s):
    s_new = re.sub(r'[.|,|?|!|;|:]+[\s]*','^',s)
    return [item for item in s_new.split('^') if item != '']

sentence_break(sample)


# In[103]:


def Position_Matrix(sentences):
    matrix = [[] for sentence in sentences]
    for i, item in enumerate(sentences):
        length = len(item.split())
        #print (length)
        for _ in range(length):
            matrix[i].append(0)
        for j, word in enumerate(item.split()):
            matrix[i][j] = format(j*1.0/(length-1),'.2f')
    return matrix
            

Position_Matrix(['1223 33 33 33 333333333333333333333','2 4'])


# In[9]:


from difflib import SequenceMatcher

s = SequenceMatcher(lambda x: x == " ",
                'Cali is good',
                'California is good')

print(round(s.ratio(), 3))
                    
for block in s.get_matching_blocks():
    print("a[%d] and b[%d] match for %d elements" % block)

    
    
import re    
def Name_Abbr_Detector(name):
    #abbr first name/last name/middle name but is not allowed to abbr all
    re.sub(r'[^/s/w]]*','',name)
    if len(name.split()) == 1:
        name_to_search = name[0].upper() + name.lower()[1:]
    elif len(name.split()) == 2: # no middle name
        first = name.split()[0]
        last = name.split()[-1]
        name_to_search = [first[0].upper + ' ' + last, first+ ' ' +last[0]]
    elif len(name.split()) == 3:
        name_to_search = []
        for pos in range(len(name.split()):
            name_to_search.append(name.split()[:pos] + name.split()[pos][0].uppper + name.split()[pos+1:])
    return name_to_search
        


# In[52]:


#preliminary design
import re    
def Name_Abbr_Detector(name):
    #abbr first name/last name/middle name but is not allowed to abbr all
    re.sub(r'[^/s/w]]*','',name)
    if len(name.split()) == 1:
        name_to_search = name[0].upper() + name.lower()[1:]
    elif len(name.split()) == 2: # no middle name
        first = name.split()[0]
        last = name.split()[-1]
        print (first, last)
        name_to_search = [first[0].upper() + ' ' + last, first +  ' ' + last[0].upper()]
    elif len(name.split()) == 3:
        name_to_search = []
        for pos in range(len(name.split())):
            
            temp_name = name.split()[:pos] + [name.split()[pos][0].upper()] + name.split()[pos+1:]
            s=''
            for item in temp_name:
                s +=  ' ' + item
            name_to_search.append(s)
    return name_to_search
Name_Abbr_Detector('Victor Henry Zhang')            
    


# In[40]:


'Victor Henry Handsome Zhang'.split()[:2] +['Zhang']


# In[ ]:


#advanced design
def Name_Abbr_Detector_Advanced(name):
    n = length(name.split())
    k = n - 1 #No.of Initials


# In[53]:


[1,2,3][:0]


# In[18]:


import inspect #The basic idea is to find
    #the longest contiguous matching subsequence that contains no "junk"
    #elements (R-O doesn't address junk)
    #As a rule of thumb, a .ratio() value over 0.6 means the
    #sequences are close matches
lines = inspect.getsourcelines(SequenceMatcher)
print("".join(lines[0]))


# In[11]:


#from abresolver import Text

