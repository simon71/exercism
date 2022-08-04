
##### 1st Option #####

# class TwoFer
#   def self.two_fer name = "you"
#       "One for #{name}, one for me."
#   end
# end

##### 2nd option #####

class TwoFer
  class << self
    def two_fer(name=nil)               # accept name or be nil
      name ||= "you"                    # name or = you
      "One for #{name}, one for me."    # return name or you
    end
  end
end
