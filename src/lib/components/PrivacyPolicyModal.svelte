<script lang="ts">
import Modal from '$lib/components/common/Modal.svelte';
import { getContext } from 'svelte';
import type { Writable } from 'svelte/store';

interface I18nStore extends Writable<any> {
	t: (key: string) => string;
}

const i18n = getContext<I18nStore>('i18n');

export let show = false;
</script>

<Modal bind:show size="md">
	<div>
		<div class="flex justify-between dark:text-gray-100 px-5 pt-4 pb-2">
			<div class="text-lg font-medium self-center font-primary">
				{$i18n.t('Privacy Policy')}
			</div>
			<button
				class="self-center"
				on:click={() => {
					show = false;
				}}
			>
				<svg
					xmlns="http://www.w3.org/2000/svg"
					viewBox="0 0 20 20"
					fill="currentColor"
					class="w-5 h-5"
				>
					<path
						d="M6.28 5.22a.75.75 0 00-1.06 1.06L8.94 10l-3.72 3.72a.75.75 0 101.06 1.06L10 11.06l3.72 3.72a.75.75 0 101.06-1.06L11.06 10l3.72-3.72a.75.75 0 00-1.06-1.06L10 8.94 6.28 5.22z"
					/>
				</svg>
			</button>
		</div>

		<div class="px-5 pb-4 dark:text-gray-200">
			<div class="prose dark:prose-invert max-w-none">
				<h2>{$i18n.t('1. Introduction')}</h2>
				<p>
					{$i18n.t('freepass.ai is committed to protecting your privacy. This Privacy Policy outlines how we collect, use, and safeguard your information when you use our Service.')}
				</p>

				<h2>{$i18n.t('2. Information We Collect')}</h2>
				<p>
					{$i18n.t('• Personal Information: We may collect information you provide directly, such as chat inputs and contact details if you choose to provide them.')}
				</p>
				<p>
					{$i18n.t('• Automatically Collected Information: This includes data like your IP address, device information, browser type, operating system, and usage data collected through cookies and similar technologies.')}
				</p>

				<h2>{$i18n.t('3. How We Use Your Information')}</h2>
				<p>
					{$i18n.t('• To Provide and Improve the Service: Ensuring the functionality and performance of freepass.ai.')}
				</p>
				<p>
					{$i18n.t('• Personalization: Tailoring content and experiences to better suit your preferences.')}
				</p>
				<p>
					{$i18n.t('• Advertising and Analytics: Delivering relevant advertisements and conducting analytical studies to enhance our offerings.')}
				</p>
				<p>
					{$i18n.t('• Communication: Sending updates, newsletters, or responding to inquiries if you provide contact information.')}
				</p>

				<h2>{$i18n.t('4. Cookies and Similar Technologies')}</h2>
				<p>
					{$i18n.t('We use cookies and similar technologies to track your interactions with freepass.ai, remember your preferences, and analyze usage patterns. You can manage your cookie preferences through your browser settings, although disabling cookies may affect the functionality of the Service.')}
				</p>

				<h2>{$i18n.t('5. Sharing and Disclosure of Information')}</h2>
				<p>
					{$i18n.t('• Third-Party Services: We may share aggregated or anonymized data with third-party service providers for analytics, advertising, or other business purposes.')}
				</p>
				<p>
					{$i18n.t('• Legal Requirements: We may disclose your information if required by law or in response to legal processes.')}
				</p>
				<p>
					{$i18n.t('• Consent: We will seek your consent before sharing any personally identifiable information with third parties, except as required by law.')}
				</p>

				<h2>{$i18n.t('6. Data Security')}</h2>
				<p>
					{$i18n.t('We implement reasonable security measures to protect your information from unauthorized access, alteration, disclosure, or destruction. However, no method of transmission over the internet or electronic storage is completely secure, and we cannot guarantee absolute security.')}
				</p>

				<h2>{$i18n.t('7. Data Retention')}</h2>
				<p>
					{$i18n.t('We retain your information only for as long as necessary to fulfill the purposes outlined in this Privacy Policy unless a longer retention period is required or permitted by law.')}
				</p>

				<h2>{$i18n.t('8. Your Rights')}</h2>
				<p>
					{$i18n.t('Depending on your jurisdiction, you may have rights regarding your personal data, including the right to access, rectify, delete, or restrict the processing of your information. To exercise these rights, please contact us at info@zaytoon.io.')}
				</p>

				<h2>{$i18n.t('9. Changes to This Privacy Policy')}</h2>
				<p>
					{$i18n.t('We may update this Privacy Policy from time to time. The "Effective Date" at the top indicates when changes were last made. Continued use of the Service after any changes constitutes acceptance of the updated Privacy Policy.')}
				</p>

				<h2>{$i18n.t('10. Children\'s Privacy')}</h2>
				<p>
					{$i18n.t('Our Service is not intended for children under the age of majority in their jurisdiction. We do not knowingly collect personal information from minors. If you become aware that a minor has provided us with personal information, please contact us, and we will take steps to remove such information.')}
				</p>

				<h2>{$i18n.t('11. International Transfers')}</h2>
				<p>
					{$i18n.t('Your information may be transferred to and processed in countries other than your own. These countries may have different data protection laws. By using the Service, you consent to the transfer of your information as described in this Privacy Policy.')}
				</p>

				<h2>{$i18n.t('12. Contact Us')}</h2>
				<p>
					{$i18n.t('If you have any questions or concerns about this Privacy Policy or our data practices, please reach out to us at info@zaytoon.io.')}
				</p>

				<h2>{$i18n.t('CONTINUED USE')}</h2>
				<p>
					{$i18n.t('By continuing to use freepass.ai, you acknowledge that you have read, understood, and agree to our Terms of Use and Privacy Policy in their current form. If you do not agree with these terms, please discontinue use of the Service.')}
				</p>
			</div>
		</div>
	</div>
</Modal>