# Real Estate Investment Potential Scorer by ZIP

A Python tool that scores ZIP codes (1-10) for real estate potential based on demographics, income, and future growth indicators.

## Quick Start

```bash
# Install dependencies
pip install -r requirements.txt

# Run the program
python flip_score.py 19125

# Or run interactively
python .py
```

## What It Does

The program analyzes ZIP codes using:

### Historical Performance (45% weight)
- **Price Appreciation (25%)** - 3-5 year price trends
- **Income Levels (15%)** - Median household income
- **Days on Market (5%)** - Sales velocity

### Future Potential (55% weight)
- **Population Growth (15%)** - Migration and growth trends
- **Employment Growth (15%)** - Job market expansion
- **Business Activity (10%)** - New business establishments
- **Infrastructure (10%)** - Education levels and amenities
- **Building Permits (5%)** - Construction activity trends

## Current Implementation

**Currently Active:**
- ✅ US Census Bureau API (free, no key required)
  - Demographics
  - Income data
  - Population statistics
  - Education levels
  - Vacancy rates

**Placeholder Data (ready for integration):**
- ⚠️ Housing price data (Zillow/Redfin/Realtor.com)
- ⚠️ Days on market metrics
- ⚠️ Employment data (BLS API)
- ⚠️ Business establishment data
- ⚠️ Building permit data

## Adding Real Data Sources

### 1. Housing Market Data

**Option A: Zillow API**
```python
# Requires application: https://www.zillow.com/howto/api/APIOverview.htm
# Add to HousingDataFetcher class
```

**Option B: Redfin Data Center**
```python
# Download historical data: https://www.redfin.com/news/data-center/
# Parse CSV files for price trends
```

**Option C: Attom Data Solutions**
```python
# API: https://api.gateway.attomdata.com/
# Paid service, comprehensive data
```

### 2. Employment Data (BLS API)

```python
# Register at: https://data.bls.gov/registrationEngine/
# Free API key
# Update EconomicDataFetcher.get_employment_data()

def get_employment_data(self, zipcode: str) -> Dict:
    # Convert ZIP to metro area
    # Fetch from BLS API
    url = "https://api.bls.gov/publicAPI/v2/timeseries/data/"
    # Series IDs for employment data
    pass
```

### 3. Building Permits

```python
# Census Building Permits Survey
# API: https://www.census.gov/construction/bps/
# Free, requires registration
```

### 4. Business Data

```python
# County Business Patterns
# API: https://api.census.gov/data/2021/cbp
# Free, same Census API key
```

## Customizing Weights
## Sample Output

```
============================================================
FLIP POTENTIAL SCORE: 7.2/10
============================================================

Recommendation: GOOD - Solid opportunity with manageable risk
Risk Level: Low-Medium

                    COMPONENT SCORES
------------------------------------------------------------

Historical Performance (45% total weight):
  Price Appreciation (25%): 7.5/10
    → Solid appreciation, good flip potential
  Income Levels (15%): 8.2/10
    → Strong buyer pool with high purchasing power
  Days on Market (5%): 6.8/10
    → Normal market velocity

Future Potential Indicators (55% total weight):
  Population Growth (15%): 7.0/10
    → Healthy population growth
  Employment Growth (15%): 7.8/10
    → Growing job market
  Business Activity (10%): 6.5/10
    → Healthy business growth
  Infrastructure (10%): 8.0/10
    → Good education levels
  Building Permits (5%): 7.0/10
    → Modest permit growth


## API Resources

- **Census API**: https://api.census.gov/data.html
- **BLS API**: https://www.bls.gov/developers/
- **Zillow**: https://www.zillow.com/howto/api/APIOverview.htm
- **Attom**: https://api.gateway.attomdata.com/
- **FBI Crime Data**: https://crime-data-explorer.fr.cloud.gov/api

## Notes

- Census data is on a 2-3 year lag (ACS 5-Year Estimates)
- Growth rates are estimated using current data as proxies
- For production use, integrate historical time series data
- Consider local market expertise alongside scores
