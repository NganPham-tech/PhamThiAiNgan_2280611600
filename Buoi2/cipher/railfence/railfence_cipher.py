class RailFenceCipher:
    def __init__(self):
        pass

    def rail_fence_encrypt(self, plain_text, num_rails):
        rails = [[] for _ in range(num_rails)]
        rail_index = 0
        direction = 1  
        for char in plain_text:
            rails[rail_index].append(char)
            if rail_index == 0:
                direction = 1
            elif rail_index == num_rails - 1:
                direction = -1
            rail_index += direction
        cipher_text = ''.join([''.join(rail) for rail in rails])
        return cipher_text


    # def rail_fence_decrypt(self, cipher_text, num_rails):
    #     rail_lengths = [0] * num_rails
    #     rail_index = 0
    #     direction = 1
    #     for _ in range(len(cipher_text)):
    #         rail_lengths[rail_index] += 1
    #         if rail_index == 0:
    #             direction = 1
    #         elif rail_index == num_rails - 1:
    #             direction = -1
    #         rail_index += direction
    #     rails = []
    #     start = 0
    #     for length in rail_lengths:
    #         rails.append(list(cipher_text[start: start + length]))
    #         start += length
    #     plain_text = ""
    #     rail_index = 0
    #     direction = 1
    #     for _ in range(len(cipher_text)):
    #         plain_text += rails[rail_index].pop(0)
    #         rails[rail_index] = rails[rail_index][1:]
    #         if rail_index == 0:
    #             direction = 1
    #         elif rail_index == num_rails - 1:
    #             direction = -1
    #         rail_index += direction

    #     return plain_text
    def rail_fence_decrypt(self, cipher_text, num_rails):
        # Step 1: Calculate rail lengths
        rail_lengths = [0] * num_rails
        rail_index = 0
        direction = 1
        for _ in range(len(cipher_text)):
            rail_lengths[rail_index] += 1
            if rail_index == 0:
                direction = 1
            elif rail_index == num_rails - 1:
                direction = -1
            rail_index += direction

        # Step 2: Fill the rails with characters from the cipher text
        rails = []
        start = 0
        for length in rail_lengths:
            rails.append(list(cipher_text[start:start + length]))
            start += length

        # Step 3: Reconstruct the plain text by reading the rails in a zigzag pattern
        plain_text = ""
        rail_index = 0
        direction = 1
        for _ in range(len(cipher_text)):
            if rails[rail_index]:
                plain_text += rails[rail_index].pop(0)
            else:
                raise ValueError(f"Attempting to pop from an empty rail at rail {rail_index}")

            if rail_index == 0:
                direction = 1
            elif rail_index == num_rails - 1:
                direction = -1
            rail_index += direction

        return plain_text