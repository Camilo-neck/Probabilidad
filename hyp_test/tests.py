import numpy as np
from scipy.stats import shapiro, chi2, ttest_1samp

def t_test(x, mu=0, conf_level=0.95, alternative='diferente'):
	"""
	Test for mean difference
	"""
	alternatives = {'diferente':'two-sided', 'menor':'less', 'mayor':'greater'}
	if alternative not in alternatives:
		raise ValueError('Invalid alternative')
	x = np.array(x)
	statistic, p = ttest_1samp(x, popmean=mu, alternative=alternatives[alternative])
	print('T-test for mean difference:')
	print('Statistics (t)=%.3f, p-value=%.5f' % (statistic, p))
	if p > 1-conf_level:
		print('Sample looks Gaussian (fail to reject H0)')
	else:
		print('Sample does not look Gaussian (reject H0)')

def test_shapiro(data: list[any]) -> None:
	"""
	Test for normality of data
	"""
	stat, p = shapiro(data)
	print('Shapiro-Wilk test for normality:')
	print('Statistics (W)=%.3f, p-value=%.3f' % (stat, p))
	if p > 0.05:
		print('Sample looks Gaussian (fail to reject H0)')
	else:
		print('Sample does not look Gaussian (reject H0)')

def test_var_chi2(s2, n, sigma2, alternative='two-sided', confidence=0.95) -> None:
	s2 = int(s2)
	n = int(n)
	# Test estadistic
	chi = (n-1)*s2/sigma2
	#p-value
	if alternative == 'two-sided':
		p1 = 1 - chi2.cdf(chi, n-1)
		p2 = chi2.cdf(chi, n-1)
		p = 2*min(p1, p2)
	elif alternative == 'less':
		p = chi2.cdf(chi, n-1)
	elif alternative == 'greater':
		p = 1-chi2.cdf(chi, n-1)
	else:
		raise ValueError('Invalid alternative')
	# Test result
	print('Chi-squared test for variance:')
	print('Statistics=%.3f, p-value=%.3f' % (chi, p))
	if p > confidence:
		print('Sample looks Gaussian (fail to reject H0)')
	else:
		print('Sample does not look Gaussian (reject H0)')

if __name__ == '__main__':
	np.random.seed(123)
	data = np.random.normal(25.5, 1, 50)
	test_shapiro(data)
	print('-----------------------------------------------------')
	test_var_chi2(np.var(data), len(data), np.var(data), 'greater', 0.95)
	print('-----------------------------------------------------')
	t_test(data, mu=25, alternative='menor')