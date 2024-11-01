def lfsr(seed, taps, length):
    """
    Generate a maximum-length LFSR sequence.

    :param seed: Initial seed (e.g., [1, 0, 0, 1])
    :param taps: Feedback taps positions (e.g., [1, 0] for x(t+1) XOR x(t))
    :param length: Length of the output sequence
    :return: LFSR output sequence
    """
    state = seed.copy()
    result = []

    for _ in range(length):
        # Store output bit (last bit of the state)
        result.append(state[-1])

        # Calculate new bit using XOR of taps positions
        new_bit = 0
        for t in taps:
            new_bit ^= state[-(t + 1)]  # taps are zero-indexed

        # Shift register and insert new bit
        state = [new_bit] + state[:-1]

    return result


# Example usage:
m = 4
seed = [1, 0, 0, 1]  # Example seed
taps = [1, 0]  # Feedback path taps for p1 and p0
length = 2 ** m - 1  # Maximum-length LFSR sequence

output_sequence = lfsr(seed, taps, length)
print("LFSR Output Sequence:", output_sequence)
