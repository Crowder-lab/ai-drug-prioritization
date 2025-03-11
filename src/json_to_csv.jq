map({
  CanonicalName: (."Canonical Name" // ""),
  CAS: (."CAS Registry Number" // ""),
  DrugLibraryName: (."Drug Library Name" // ""),
  HaveIt: (.["Have It"] // ""),
  Screened: (.Screened // ""),
  NotInDrugBank: (.["Not In DrugBank"] // ""),
  FDAApproved: (.["FDA Approved"] // ""),
  Indication: (.Indication // ""),
  Mechanism: (.Mechanism // ""),
  DrugBankName: (."DrugBank Name" // ""),
  Price: (.Price // [] | join("; ")),
  SMILES: (.SMILES // ""),
  UNII: (.UNII // ""),
  BloodBrainBarrier: (."Blood Brain Barrier" // "")
}) 
| (map(keys) | add | unique) as $cols 
| ($cols | join(",")) 
, (map([.[ $cols[] ]] | @csv) | .[])
