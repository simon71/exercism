class ResistorColorDuo
  class << self

    def stripes
      @stripes = {
        '0' => "black",
        '1' => "brown",
        '2' => "red",
        '3' => "orange",
        '4' => "yellow",
        '5' => "green",
        '6' => "blue",
        '7' => "violet",
        '8' => "grey",
        '9' => "white"
      }
    end

    def value(colors)
      stripes
      resist=[]
      colors.first(2).map do |c|
        resist.append(stripes.key(c))
      end
      resist.join.to_i
    end
  end
end
