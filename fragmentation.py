# IP Fragmentation Simulator
# Calculates how IP packets are fragmented based on MTU and header size

def posa_tmhmata(mhkos_paketoy, mtu):
    """Υπολογίζει πόσα τμήματα χρειάζονται για την αποστολή του πακέτου."""
    tmhmata = mhkos_paketoy / (mtu - 20)
    if tmhmata == int(tmhmata):
        return int(tmhmata)
    else:
        return int(tmhmata) + 1

def prwtos_pinakas(tmhmata):
    return [f"{i}ο τμήμα" for i in range(1, tmhmata + 1)]

def mikos_epikefalidas(epikefalida, tmhmata):
    return [f"{epikefalida}" for _ in range(tmhmata)]

def mhkos_dedomenwn(synoliko_mhkos, mtu, epikefalida, tmhmata):
    """Υπολογισμός μεγέθους δεδομένων κάθε τμήματος."""
    offset = int((mtu - epikefalida) / 8.0)
    dedomena = [offset * 8] * (tmhmata - 1)
    teliko = synoliko_mhkos - (offset * 8 * (tmhmata - 1)) - 20
    dedomena.append(teliko)
    return dedomena, offset

def synoliko_mhkos_pinatakas(dedomena):
    return [d + 20 for d in dedomena]

def anagnoristiko(anagnor, tmhmata):
    return [anagnor] * tmhmata

def dont_fragment_flag(tmhmata):
    return [0] * tmhmata

def more_fragment_flag(tmhmata):
    return [1] * (tmhmata - 1) + [0]

def fragment_offset_list(offset_step, tmhmata):
    return [i * offset_step for i in range(tmhmata)]

def ektupwsi_pinaka(headers, *columns):
    print(" | ".join(headers))
    print("-" * 80)
    for i in range(len(columns[0])):
        row = " | ".join(f"{col[i]}" for col in columns)
        print(row)

# ------------------------ Κύριο πρόγραμμα ----------------------------

# Είσοδοι
mhkos_paketoy = 4000    # συνολικό μήκος IP πακέτου (bytes)
mtu = 1500              # Maximum Transmission Unit (bytes)
epikefalida = 20        # Μήκος επικεφαλίδας (bytes)
anagnor = 12345         # ID του πακέτου

# Υπολογισμοί
tmhmata = posa_tmhmata(mhkos_paketoy, mtu)
tmhmata_names = prwtos_pinakas(tmhmata)
header_lengths = mikos_epikefalidas(epikefalida, tmhmata)
dedomena, offset_step = mhkos_dedomenwn(mhkos_paketoy, mtu, epikefalida, tmhmata)
syn_mhkoi = synoliko_mhkos_pinatakas(dedomena)
ids = anagnoristiko(anagnor, tmhmata)
df = dont_fragment_flag(tmhmata)
mf = more_fragment_flag(tmhmata)
offsets = fragment_offset_list(offset_step, tmhmata)

# Εμφάνιση
headers = [
    "Τμήμα", "Μήκος Επικεφαλίδας", "Συνολικό Μήκος",
    "Μήκος Δεδομένων", "Αναγνωριστικό", "DF", "MF", "Fragment Offset"
]
ektupwsi_pinaka(
    headers,
    tmhmata_names, header_lengths, syn_mhkoi,
    dedomena, ids, df, mf, offsets
)
