# frozen_string_literal: true

# This class create a matrix from a given array
class Matrix
  attr_reader :rows
  attr_reader :columns

  def initialize(matrix)
    @rows = String(matrix).split(/\n/).map { |r| r.split.map(&:to_i) }
    @columns = @rows.transpose
  end

  ## Long way ##
  # This method assumes what's passed in is an array of arrays
  # It also assumes its a true matrix i.e each row is the same length
  # def transpose_array(_array)
  #   columns = []
  #   i = 0
  #   while i < @rows.first.size
  #     j = 0
  #     columns[i] = []
  #     while j < @rows.size
  #       columns[i] << @rows[j][i]
  #       j += 1
  #     end

  #     i += 1

  #   end
  #   columns
  # end
end
