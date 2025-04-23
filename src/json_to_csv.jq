map({
  CanonicalName: (."Canonical Name" // ""),
  DrugLibraryName: (."Drug Library Name" // ""),
  DrugBankName: (."DrugBank Name" // ""),
  CAS: (."CAS Registry Number" // ""),
  UNII: (.UNII // ""),
  SMILES: (.SMILES // ""),
  HaveIt: (.["Have It"] // ""),
  Screened: (.Screened // ""),
  RepurposingCategory: (."Repurposing Category" // ""),
  RepurposingContinued: (."Repurposing Continued" // ""),
  Indication: (.Indication // ""),
  Mechanism: (.Mechanism // ""),
  BloodBrainBarrier: (."Blood Brain Barrier" // ""),
  Bioavailability: (."Bioavailability" // ""),
  HumanIntestinalAbsorption: (."Human Intestinal Absorption" // ""),
  FDAApproved: (.["FDA Approved"] // ""),
  Price: (.Price // [] | join("; ")),
  NotInDrugBank: (.["Not In DrugBank"] // ""),
  RBPediatricSafety: (."RB Case Reports/Pediatric Safety" // ""),
  RBSideEffects: (."RB Side Effects/Adverse Events" // ""),
  RBBioavailability: (."RB Bioavailability " // ""),
  RBLinks: (."RB Links" // ""),
  EDSideEffectRank: (."ED Side Effect Rank" // ""),
  EDPediatricSafety: (."ED Pediatric Safety" // ""),
}) 
| (map(keys) | add | unique) as $cols 
| ($cols | join(",")) 
, (map([.[ $cols[] ]] | @csv) | .[])
