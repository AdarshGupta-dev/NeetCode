import bisect


class TimeMap:

    def __init__(self):
        # Dictionary to store key -> ([timestamps], [values])
        # Each key maps to a tuple of two lists:
        # - The first list stores the timestamps
        # - The second list stores the corresponding values for each timestamp
        self._data = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        # Check if the key already exists in the dictionary
        if key in self._data:
            # If it exists, append the new timestamp and value to the respective lists
            self._data[key][0].append(timestamp)  # Append to timestamps
            self._data[key][1].append(value)  # Append to values
        else:
            # If the key doesn't exist, initialize the key with two lists:
            # - One for storing the timestamps
            # - Another for storing the corresponding values
            self._data[key] = [timestamp], [value]

    def get(self, key: str, timestamp: int) -> str:
        # Check if the key exists in the dictionary
        if key in self._data:
            # Perform a binary search using bisect_right to find the right position
            # in the timestamp list where the given timestamp would fit.
            # This ensures we find the most recent timestamp <= the input timestamp.
            idx = bisect.bisect_right(self._data[key][0], timestamp) - 1

            # If idx >= 0, it means there is a valid timestamp <= the input timestamp
            if idx >= 0:
                # Return the corresponding value for the found timestamp
                return self._data[key][1][idx]

        # If the key doesn't exist or no valid timestamp <= input timestamp is found,
        # return an empty string
        return ""
