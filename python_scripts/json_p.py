import json


with open("data_file_2.json", "r") as read_file:
    data = json.load(read_file)

print(read_file)

# blackjack_hand = (8, "Q")
# encoded_hand = json.dumps(blackjack_hand)
# decoded_hand = json.loads(encoded_hand)
#
# print(blackjack_hand == decoded_hand)
# print("\n")
# print(type(blackjack_hand))
# print(blackjack_hand)
# print(type(decoded_hand))
# print(decoded_hand)
# print("\n")
# print(blackjack_hand == tuple(decoded_hand))

# data = {
#     "president": {
#         "name": "Zaphod Beeblebrox",
#         "species": "Betelgeusian"
#     }
# }
#
# with open("data_file_2.json", "w") as write_file:
#     json.dump(data, write_file)
#
# # json_string = json.dumps(data)
# json_string = json.dumps(data, indent=4)
# print(json_string)
