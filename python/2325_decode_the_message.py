class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        # dict is sorted by default
        key_dict = {' ':' '}

        uniq_key_idx = 0
        for k in key:
            if k not in key_dict:
                # chr... := consecutive letters
                key_dict[k] = chr(ord('a')+uniq_key_idx)
                uniq_key_idx += 1

        decrypted_message = []
        for letter in message:
            decrypted_message.append(key_dict[letter])

        return "".join(decrypted_message)
