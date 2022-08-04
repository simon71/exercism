class Hamming
  class << self
    def compute(strand1, strand2)
      raise ArgumentError unless strand1.length == strand2.length

      count = 0

      strand1.split('').each_with_index do |char, index|
        count += 1 if char != strand2[index]
      end

      count
    end
  end
end
