# zbiór MID-ów (jakichś tam m-identyfikatorów) - zakładamy, że nie znamy tych danych (przychodzą np. z innego świata)
tech_mids = [130, 253, 207, 309, 275, 184, 144, 154, 174, 271, 216, 272, 152, 238, 205, 139, 182, 170, 202, 223, 287, 155, 304, 153, 212, 268, 299, 249, 237, 224, 228, 148, 248, 165, 288, 210, 294, 185, 187, 250, 164, 168, 215, 231, 263, 278, 229, 160, 124, 307, 286, 267, 290, 318, 189, 265, 232, 220, 301, 317, 295, 137, 200, 132, 314, 239, 311, 303, 247, 261, 269, 191, 245, 281, 293, 123, 242, 214, 284, 178, 258, 129, 208, 291, 241, 133, 305, 169, 321, 146, 211, 196, 316, 158, 151, 234, -1, 173, 192, 310, 135, 262, 194, 166, 280, 183, 159, 217, 319, 244, 179, 297, 157, 259, 190, 226, 296, 131, 162, 204, 186, 252, 227, 140, 298, 161, 264, 195, 243, 308, 504, 320, 134, 126, 225, 145, 138, 141, 180, 255, 201, 274, 222, 276, 500, 292, 270, 306, 246, 218, 197, 254, 188, 285, 315, 143, 251, 256, 156, 260, 209, 219, 176, 193, 147, 171, 206, 125, 175, 312, 128, 149, 127, 273, 150, 167, 283, 302, 172, 282, 277, 235, 198, 300, 199, 240, 177, 181, 163, 142, 236, 221, 289, 313, 257, 203, 230, 266, 233, 136, 279, 213]

## tu zaczyna się nasz kod

# zliczamy i grupujemy tylko te "dobre" (od 100 do 399)
tech_mids_cnt = 0
tech_mid_1xx_group_cnt = 0
tech_mid_2xx_group_cnt = 0
tech_mid_3xx_group_cnt = 0
for tech_mid in tech_mids:
    tech_mids_cnt += 1
    if 400 > tech_mid >= 300:
        tech_mid_3xx_group_cnt += 1
    elif 300 > tech_mid >= 200:
        tech_mid_2xx_group_cnt += 1
    elif 200 > tech_mid >= 100:
        tech_mid_1xx_group_cnt += 1
    else:
        print('Wrong MID:', tech_mid)

# przy nieparzystej liczbie MID-ów środkowy MID (~mediana)
if tech_mids_cnt % 2 == 1:
    tech_mid = tech_mids[tech_mids_cnt / 2]

print('Good MIDs (total):', tech_mids_cnt)
print('- 1xx MIDs:', tech_mid_1xx_group_cnt)
print('- 2xx MIDs:', tech_mid_2xx_group_cnt)
print('- 3xx MIDs:', tech_mid_3xx_group_cnt)
print('- mid-MID:', tech_mid)

