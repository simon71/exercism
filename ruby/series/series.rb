class Series
  def initialize(series)
    @digits = String(series).split('')
  end

  def slices(size)
    raise ArgumentError if size > @digits.size
    
    @digits.each_cons(size).map(&:join)

  end
end
